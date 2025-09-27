import importlib
import sys
import types
from pathlib import Path

import talon


if hasattr(talon, "test_mode"):
    from unittest.mock import MagicMock

    from talon import actions

    from core.numbers import numbers

    PROJECT_ROOT = Path(__file__).resolve().parents[1]


    def _ensure_namespace_package(name: str, path: Path) -> None:
        if name in sys.modules:
            return

        module = types.ModuleType(name)
        module.__path__ = [str(path)]
        sys.modules[name] = module


    _ensure_namespace_package("talon_community", PROJECT_ROOT)
    _ensure_namespace_package("talon_community.lang", PROJECT_ROOT / "lang")
    _ensure_namespace_package("talon_community.core", PROJECT_ROOT / "core")
    _ensure_namespace_package("talon_community.lang.gdscript", PROJECT_ROOT / "lang" / "gdscript")

    gdscript_module = importlib.import_module("talon_community.lang.gdscript.gdscript")


    class FakeMatch(list):
        def __init__(self, first_value, **attributes):
            super().__init__([first_value])
            for name, value in attributes.items():
                setattr(self, name, value)


    def setup_function():
        actions.reset_test_actions()


    def _assert_randf_range(minimum_match: FakeMatch, maximum_match: FakeMatch, expected: str) -> None:
        mock_insert = MagicMock()
        actions.register_test_action("", "insert", mock_insert)

        minimum = numbers.number_prose_unprefixed_first(minimum_match)
        maximum = numbers.number_prose_unprefixed_second(maximum_match)

        gdscript_module.UserActions.gdscript_random_float(minimum, maximum)

        mock_insert.assert_called_once_with(expected)


    def test_number_prose_unprefixed_supports_repeated_captures():
        match = FakeMatch("WRONG", number_prose_with_dot_1="2.5")

        assert numbers.number_prose_unprefixed(match) == "2.5"


    def test_random_float_integers():
        _assert_randf_range(
            FakeMatch("1", number_signed_string="1"),
            FakeMatch("WRONG", number_signed_string_1="3"),
            "randf_range(1, 3)",
        )


    def test_random_float_decimals():
        _assert_randf_range(
            FakeMatch("WRONG", number_prose_with_dot="0.5"),
            FakeMatch("WRONG", number_prose_with_dot_1="2.5"),
            "randf_range(0.5, 2.5)",
        )


    def test_number_prose_unprefixed_wrappers_support_repeated_captures():
        first = FakeMatch("WRONG", number_prose_with_dot="0.5")
        second = FakeMatch("WRONG", number_prose_with_dot_1="2.5")

        assert numbers.number_prose_unprefixed_first(first) == "0.5"
        assert numbers.number_prose_unprefixed_second(second) == "2.5"
