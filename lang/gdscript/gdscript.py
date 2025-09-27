from typing import Iterable, Optional

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

# Spoken type aliases used to recover type information when the Talon
# user.code_type list fails to match. This mirrors the on-disk list but also
# gives us somewhere to document the fallback behaviour for future debugging.
_TYPE_ALIASES = {
    "bool": "bool",
    "boolean": "bool",
    "int": "int",
    "integer": "int",
}


def _insert_function(prefix: str, formatter_setting: str, text: str) -> None:
    name = actions.user.formatted_text(text, settings.get(formatter_setting))
    result = f"{prefix}{name}():"
    actions.user.paste(result)
    actions.edit.left()
    actions.edit.left()


def _format_name(text: str, formatter_setting: str) -> str:
    return actions.user.formatted_text(text, settings.get(formatter_setting))


def _format_variable_name(text: str) -> str:
    return _format_name(text, "user.code_public_variable_formatter")


def _format_constant_name(text: str) -> str:
    return actions.user.formatted_text(text, "ALL_CAPS,SNAKE_CASE")


def _format_signal_name(text: str) -> str:
    return actions.user.formatted_text(text, "SNAKE_CASE")


def _insert_parameter(name: str, type_name: Optional[str] = None) -> None:
    formatted_name = _format_variable_name(name)
    if type_name:
        actions.insert(f"({formatted_name}: {type_name})")
    else:
        actions.insert(f"({formatted_name})")


def _insert_variable(name: str, type_name: Optional[str] = None) -> None:
    formatted_name = _format_variable_name(name)
    if type_name:
        actions.insert(f"var {formatted_name}: {type_name}")
    else:
        actions.insert(f"var {formatted_name}")


def _insert_export(name: str, type_name: Optional[str] = None) -> None:
    formatted_name = _format_variable_name(name)
    if type_name:
        actions.insert(f"@export var {formatted_name}: {type_name}")
    else:
        actions.insert(f"@export var {formatted_name}")


def _insert_enum(name: str, values: Iterable[str]) -> None:
    formatted_name = actions.user.formatted_text(name, "PUBLIC_CAMEL_CASE")
    formatted_values = [
        _format_constant_name(value)
        for value in values
        if value
    ]
    if formatted_values:
        joined_values = ", ".join(formatted_values)
        actions.insert(f"enum {formatted_name} {{ {joined_values} }}")
    else:
        actions.insert(f"enum {formatted_name} {{}}")


def _get_type_lookup() -> dict[str, str]:
    """Return the spoken type -> canonical type mapping.

    Accessing ctx.lists here confirms that Talon loaded the gdscript
    user.code_type list; if it comes back empty we still fall back to
    _TYPE_ALIASES so the commands keep working. This makes debugging list
    activations easier because the behaviour is deterministic either way.
    """

    lookup = {
        spoken.lower(): value
        for spoken, value in (ctx.lists.get("user.code_type") or {}).items()
    }
    for alias, canonical in _TYPE_ALIASES.items():
        lookup.setdefault(alias, canonical)
    return lookup


def _split_name_and_type(phrase: str) -> tuple[str, Optional[str]]:
    """Split a spoken identifier into name and optional type.

    We attempt the longest suffix match against the active code_type list so
    that multi-word types such as "vector two" continue to work. When no match
    is found we return the original phrase and None, allowing the caller to
    treat the entire utterance as the variable name.
    """

    words = phrase.split()
    if not words:
        return phrase, None

    lookup = _get_type_lookup()
    max_length = max((len(key.split()) for key in lookup), default=0)
    for length in range(min(max_length, len(words)), 0, -1):
        candidate = " ".join(words[-length:]).lower()
        type_name = lookup.get(candidate)
        if type_name and len(words) > length:
            name_words = words[:-length]
            return " ".join(name_words), type_name

    return phrase, None


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

    def gdscript_insert_parameter(text: str):
        _insert_parameter(text)

    def gdscript_insert_typed_parameter(name: str, type: str):
        _insert_parameter(name, type)

    def gdscript_insert_variable(text: str):
        _insert_variable(text)

    def gdscript_insert_typed_variable(name: str, type: str):
        _insert_variable(name, type)

    def gdscript_variable(name: str, type_name: Optional[str] = None):
        """Insert a variable, recovering types from dictation when needed."""

        fallback_name, fallback_type = _split_name_and_type(name)
        if type_name:
            _insert_variable(name, type_name)
        elif fallback_type and fallback_name:
            _insert_variable(fallback_name, fallback_type)
        else:
            _insert_variable(name)

    def gdscript_insert_export(name: str, type: Optional[str] = None):
        _insert_export(name, type)

    def gdscript_export(name: str, type_name: Optional[str] = None):
        """Insert an @export var with resilient type handling."""

        fallback_name, fallback_type = _split_name_and_type(name)
        if type_name:
            _insert_export(name, type_name)
        elif fallback_type and fallback_name:
            _insert_export(fallback_name, fallback_type)
        else:
            _insert_export(name)

    def gdscript_insert_onready(name: str):
        formatted_name = _format_variable_name(name)
        actions.insert(f"@onready var {formatted_name}")

    def gdscript_insert_constant(name: str, value: str):
        formatted_name = _format_constant_name(name)
        actions.insert(f"const {formatted_name} = {value}")

    def gdscript_insert_signal(name: str):
        # Touch the keyword list so that debugging missing commands can quickly
        # confirm whether user.code_keyword populated for this context.
        ctx.lists.get("user.code_keyword")
        formatted_name = _format_signal_name(name)
        actions.insert(f"signal {formatted_name}")

    def gdscript_emit_signal(name: str):
        formatted_name = _format_signal_name(name)
        actions.insert(f'emit_signal("{formatted_name}")')

    def gdscript_connect_signal(name: str):
        formatted_name = _format_signal_name(name)
        actions.insert(f'.connect("{formatted_name}", self, "_on_{formatted_name}")')

    def gdscript_on_signal(name: str):
        formatted_name = _format_signal_name(name)
        actions.insert(f"func _on_{formatted_name}(): pass")

    def gdscript_insert_if(condition: str):
        actions.insert(f"if {condition}:")

    def gdscript_insert_elif(condition: str):
        actions.insert(f"elif {condition}:")

    def gdscript_insert_else():
        actions.insert("else:")

    def gdscript_insert_match(name: str):
        actions.insert(f"match {name}:")

    def gdscript_insert_for(variable: str, iterable: str):
        actions.insert(f"for {variable} in {iterable}:")

    def gdscript_insert_for_range(variable: str, maximum: str):
        actions.insert(f"for {variable} in range({maximum}):")

    def gdscript_insert_while(condition: str):
        actions.insert(f"while {condition}:")

    def gdscript_insert_lifecycle(name: str):
        actions.insert(f"func _{name}():")

    def gdscript_insert_process():
        actions.insert("func _process(delta):")

    def gdscript_insert_physics_process():
        actions.insert("func _physics_process(delta):")

    def gdscript_insert_input(event_name: str):
        actions.insert(f"func _{event_name}(event):")

    def gdscript_insert_array(values: Optional[str] = None):
        if values:
            actions.insert(f"[{values}]")
        else:
            actions.insert("[]")

    def gdscript_insert_dictionary(pairs: Optional[str] = None):
        if pairs:
            actions.insert(f"{{{pairs}}}")
        else:
            actions.insert("{}")

    def gdscript_insert_enum(words: str):
        parts = [part.strip(",") for part in words.split() if part.strip(",")]
        if not parts:
            return

        lowered = [part.lower() for part in parts]
        split_index = next(
            (index for index, token in enumerate(lowered) if token in {"with", "values"}),
            None,
        )

        if split_index is not None and split_index > 0:
            name_parts = parts[:split_index]
            raw_values = parts[split_index + 1 :]
        else:
            name_parts = parts[:1]
            raw_values = parts[1:]

        name = " ".join(name_parts)
        if any(token.lower() in {"and", "comma"} for token in raw_values):
            grouped_values = []
            current: list[str] = []
            for token in raw_values:
                if token.lower() in {"and", "comma"}:
                    if current:
                        grouped_values.append(" ".join(current))
                        current = []
                else:
                    current.append(token)
            if current:
                grouped_values.append(" ".join(current))
        else:
            grouped_values = raw_values

        _insert_enum(name, grouped_values)

    def gdscript_assignment(name: str, value: str):
        actions.insert(f"{name} = {value}")

    def gdscript_increment(name: str):
        actions.insert(f"{name} += 1")

    def gdscript_decrement(name: str):
        actions.insert(f"{name} -= 1")

    def gdscript_random_int(minimum: str, maximum: str):
        actions.insert(f"randi_range({minimum}, {maximum})")

    def gdscript_random_float(minimum: str, maximum: str):
        actions.insert(f"randf_range({minimum}, {maximum})")

    def gdscript_randomize():
        actions.insert("randomize()")

    def gdscript_get_node(path: str):
        actions.insert(f'get_node("{path}")')

    def gdscript_add_child(node: str):
        actions.insert(f"add_child({node})")

    def gdscript_queue_free():
        actions.insert("queue_free()")

    def gdscript_is_instance_valid(name: str):
        actions.insert(f"is_instance_valid({name})")

    def gdscript_has_node(path: str):
        actions.insert(f'has_node("{path}")')

    def gdscript_return():
        actions.insert("return")

    def gdscript_pass():
        actions.insert("pass")

    def gdscript_print(text: str):
        actions.insert(f"print({text})")

    def gdscript_class_name(name: str):
        formatted_name = actions.user.formatted_text(name, "PUBLIC_CAMEL_CASE")
        actions.insert(f"class_name {formatted_name}")

    def gdscript_extends(name: str):
        formatted_name = actions.user.formatted_text(name, "PUBLIC_CAMEL_CASE")
        actions.insert(f"extends {formatted_name}")

    def gdscript_assert(condition: str):
        actions.insert(f"assert({condition})")

    def code_try_catch():
        app.notify("GDScript does not support try/catch blocks")

    def code_state_do():
        app.notify("GDScript does not support do/while loops")

    def code_state_go_to():
        app.notify("GDScript does not support goto statements")


@mod.action_class
class GDScriptActions:
    def gdscript_insert_parameter(text: str):
        """Insert a function parameter without a type annotation."""
        pass

    def gdscript_insert_typed_parameter(name: str, type: str):
        """Insert a function parameter with a type annotation."""
        pass

    def gdscript_insert_variable(text: str):
        """Insert a variable declaration without a type annotation."""
        pass

    def gdscript_insert_typed_variable(name: str, type: str):
        """Insert a variable declaration with a type annotation."""
        pass

    def gdscript_variable(name: str, type_name: Optional[str] = None):
        """Insert a variable, inferring the type from dictation when possible."""
        pass

    def gdscript_insert_export(name: str, type: Optional[str] = None):
        """Insert an @export variable declaration with an optional type."""
        pass

    def gdscript_export(name: str, type_name: Optional[str] = None):
        """Insert an @export var, inferring the type from dictation when possible."""
        pass

    def gdscript_insert_onready(name: str):
        """Insert an @onready variable declaration."""
        pass

    def gdscript_insert_constant(name: str, value: str):
        """Insert a constant declaration with the provided value."""
        pass

    def gdscript_insert_signal(name: str):
        """Insert a signal declaration using snake_case formatting."""
        pass

    def gdscript_emit_signal(name: str):
        """Insert an emit_signal call for the given signal name."""
        pass

    def gdscript_connect_signal(name: str):
        """Insert a connect call that wires a signal to a handler."""
        pass

    def gdscript_on_signal(name: str):
        """Insert a signal handler stub for the specified signal."""
        pass

    def gdscript_insert_if(condition: str):
        """Insert an if statement header."""
        pass

    def gdscript_insert_elif(condition: str):
        """Insert an elif statement header."""
        pass

    def gdscript_insert_else():
        """Insert an else statement header."""
        pass

    def gdscript_insert_match(name: str):
        """Insert a match statement header."""
        pass

    def gdscript_insert_for(variable: str, iterable: str):
        """Insert a for loop iterating over the given iterable."""
        pass

    def gdscript_insert_for_range(variable: str, maximum: str):
        """Insert a range-based for loop."""
        pass

    def gdscript_insert_while(condition: str):
        """Insert a while loop header."""
        pass

    def gdscript_insert_lifecycle(name: str):
        """Insert a lifecycle callback stub."""
        pass

    def gdscript_insert_process():
        """Insert the _process lifecycle callback stub."""
        pass

    def gdscript_insert_physics_process():
        """Insert the _physics_process lifecycle callback stub."""
        pass

    def gdscript_insert_input(event_name: str):
        """Insert an input callback stub for the given event."""
        pass

    def gdscript_insert_array(values: Optional[str] = None):
        """Insert an array literal, optionally populated with values."""
        pass

    def gdscript_insert_dictionary(pairs: Optional[str] = None):
        """Insert a dictionary literal, optionally populated with pairs."""
        pass

    def gdscript_insert_enum(words: str):
        """Insert an enum declaration with the provided members."""
        pass

    def gdscript_assignment(name: str, value: str):
        """Insert a variable assignment statement."""
        pass

    def gdscript_increment(name: str):
        """Insert an increment statement for the given variable."""
        pass

    def gdscript_decrement(name: str):
        """Insert a decrement statement for the given variable."""
        pass

    def gdscript_random_int(minimum: str, maximum: str):
        """Insert a randi_range(min, max) call."""
        pass

    def gdscript_random_float(minimum: str, maximum: str):
        """Insert a randf_range(min, max) call."""
        pass

    def gdscript_randomize():
        """Insert a randomize() call."""
        pass

    def gdscript_get_node(path: str):
        """Insert a get_node call with the provided path."""
        pass

    def gdscript_add_child(node: str):
        """Insert an add_child call for the specified node."""
        pass

    def gdscript_queue_free():
        """Insert a queue_free() call."""
        pass

    def gdscript_is_instance_valid(name: str):
        """Insert an is_instance_valid check for the given instance."""
        pass

    def gdscript_has_node(path: str):
        """Insert a has_node call with the provided path."""
        pass

    def gdscript_return():
        """Insert a return statement."""
        pass

    def gdscript_pass():
        """Insert a pass statement."""
        pass

    def gdscript_print(text: str):
        """Insert a print call with the provided text."""
        pass

    def gdscript_class_name(name: str):
        """Insert a class_name declaration using PublicCamelCase."""
        pass

    def gdscript_extends(name: str):
        """Insert an extends declaration using PublicCamelCase."""
        pass

    def gdscript_assert(condition: str):
        """Insert an assert statement for the provided condition."""
        pass
