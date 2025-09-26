from talon import Context, Module, actions, app, settings

from ...core.described_functions import create_described_insert_between
from ..tags.operators import Operators

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: gdscript
"""

operators = Operators(
    # code_operators_array
    SUBSCRIPT=create_described_insert_between("[", "]"),
    # code_operators_assignment
    ASSIGNMENT=" = ",
    ASSIGNMENT_SUBTRACTION=" -= ",
    ASSIGNMENT_ADDITION=" += ",
    ASSIGNMENT_MULTIPLICATION=" *= ",
    ASSIGNMENT_DIVISION=" /= ",
    ASSIGNMENT_MODULO=" %= ",
    ASSIGNMENT_INCREMENT=" += 1",
    ASSIGNMENT_BITWISE_AND=" &= ",
    ASSIGNMENT_BITWISE_OR=" |= ",
    ASSIGNMENT_BITWISE_EXCLUSIVE_OR=" ^= ",
    ASSIGNMENT_BITWISE_LEFT_SHIFT=" <<= ",
    ASSIGNMENT_BITWISE_RIGHT_SHIFT=" >>= ",
    # code_operators_bitwise
    BITWISE_NOT="~",
    BITWISE_AND=" & ",
    BITWISE_OR=" | ",
    BITWISE_EXCLUSIVE_OR=" ^ ",
    BITWISE_LEFT_SHIFT=" << ",
    BITWISE_RIGHT_SHIFT=" >> ",
    # code_operators_math
    MATH_SUBTRACT=" - ",
    MATH_ADD=" + ",
    MATH_MULTIPLY=" * ",
    MATH_DIVIDE=" / ",
    MATH_INTEGER_DIVIDE=" // ",
    MATH_MODULO=" % ",
    MATH_EXPONENT=" ** ",
    MATH_EQUAL=" == ",
    MATH_NOT_EQUAL=" != ",
    MATH_GREATER_THAN=" > ",
    MATH_GREATER_THAN_OR_EQUAL=" >= ",
    MATH_LESS_THAN=" < ",
    MATH_LESS_THAN_OR_EQUAL=" <= ",
    MATH_AND=" and ",
    MATH_OR=" or ",
    MATH_NOT=" not ",
    MATH_IN=" in ",
    MATH_NOT_IN=" not in ",
)


def _insert_function(prefix: str, formatter_setting: str, text: str) -> None:
    name = actions.user.formatted_text(text, settings.get(formatter_setting))
    result = f"{prefix}{name}():"
    actions.user.paste(result)
    actions.edit.left()
    actions.edit.left()


@ctx.action_class("user")
class UserActions:
    def code_get_operators() -> Operators:
        return operators

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_self():
        actions.auto_insert("self")

    def code_insert_null():
        actions.auto_insert("null")

    def code_insert_is_null():
        actions.auto_insert(" == null")

    def code_insert_is_not_null():
        actions.auto_insert(" != null")

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    def code_insert_function(text: str, selection: str):
        name = actions.user.formatted_text(
            text, settings.get("user.code_public_function_formatter")
        )
        if selection:
            actions.user.paste(f"{name}({selection})")
        else:
            actions.user.paste(f"{name}()")
        actions.edit.left()

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        _insert_function("func _", "user.code_private_function_formatter", text)

    def code_public_function(text: str):
        _insert_function("func ", "user.code_public_function_formatter", text)

    def code_public_static_function(text: str):
        _insert_function("static func ", "user.code_public_function_formatter", text)

    def code_private_static_function(text: str):
        _insert_function("static func _", "user.code_private_function_formatter", text)

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")

    def code_insert_named_argument(parameter_name: str):
        actions.insert(f"{parameter_name}: ")

    def code_try_catch():
        app.notify("GDScript does not support try/catch blocks")

    def code_state_do():
        app.notify("GDScript does not support do/while loops")

    def code_state_go_to():
        app.notify("GDScript does not support goto statements")
