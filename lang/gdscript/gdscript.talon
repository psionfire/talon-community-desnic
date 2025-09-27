code.language: gdscript
-

# Core language tags
# -------------------
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_comment_documentation
tag(): user.code_comment_line
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

# Sample commands
# ---------------
state extends <user.text>:
    user.gdscript_extends(text)

state class name <user.text>:
    user.gdscript_class_name(text)

# The signal command stays simple, but the action itself now has additional
# validation to cope with missing list data; see gdscript.py for details.
signal <user.text>:
    user.gdscript_insert_signal(text)

state on ready (var | variable) <user.text>:
    user.gdscript_insert_onready(text)

function <user.text>:
    user.code_public_function(text)

private function <user.text>:
    user.code_private_function(text)

static function <user.text>:
    user.code_public_static_function(text)

private static function <user.text>:
    user.code_private_static_function(text)

parameter <user.text>$:
    user.gdscript_insert_parameter(text)

parameter <user.text> <user.code_type>:
    user.gdscript_insert_typed_parameter(text, code_type)

return type <user.code_type>:
    user.code_insert_return_type(code_type)

# When the type capture fails we fall back to parsing the spoken text so that
# phrases like "variable health int" still work.
variable <user.text>$:
    user.gdscript_variable(text)

# Explicit capture of user.code_type is still supported. The Python helper
# consolidates the logic so both paths behave consistently.
variable <user.text> <user.code_type>:
    user.gdscript_variable(text, code_type)

# Export supports the same fallback behaviour as variables; the helper will
# attempt to recover the type from dictation if the capture is empty.
export int <user.text>:
    user.gdscript_export(text, "int")

export float <user.text>:
    user.gdscript_export(text, "float")

export bool <user.text>:
    user.gdscript_export(text, "bool")

# Spoken fallback for @export when no code_type capture fires. This mirrors the
# variable fallback, allowing commands like "export speed int".
export <user.text>$:
    user.gdscript_export(text)

onready var <user.text>:
    user.gdscript_insert_onready(text)

const <user.text> = <user.text>:
    user.gdscript_insert_constant(text, text_1)

emit signal <user.text>:
    user.gdscript_emit_signal(text)

connect signal <user.text>:
    user.gdscript_connect_signal(text)

on signal <user.text>:
    user.gdscript_on_signal(text)

if <user.text>:
    user.gdscript_insert_if(text)

elif <user.text>:
    user.gdscript_insert_elif(text)

else:
    user.gdscript_insert_else()

match <user.text>:
    user.gdscript_insert_match(text)

for <user.text> in <user.text>:
    user.gdscript_insert_for(text, text_1)

for <user.text> in range <number>:
    user.gdscript_insert_for_range(text, number)

while <user.text>:
    user.gdscript_insert_while(text)

init:
    user.gdscript_insert_lifecycle("init")

ready:
    user.gdscript_insert_lifecycle("ready")

enter tree:
    user.gdscript_insert_lifecycle("enter_tree")

exit tree:
    user.gdscript_insert_lifecycle("exit_tree")

process:
    user.gdscript_insert_process()

physics process:
    user.gdscript_insert_physics_process()

input event:
    user.gdscript_insert_input("input")

unhandled input event:
    user.gdscript_insert_input("unhandled_input")

empty array:
    user.gdscript_insert_array()

array <user.text>:
    user.gdscript_insert_array(text)

empty dictionary:
    user.gdscript_insert_dictionary()

dictionary <user.text>:
    user.gdscript_insert_dictionary(text)

enum <user.text>:
    user.gdscript_insert_enum(text)

set <user.text> equals <user.text>:
    user.gdscript_assignment(text, text_1)

increment <user.text>:
    user.gdscript_increment(text)

decrement <user.text>:
    user.gdscript_decrement(text)

# Talon numbers repeated captures starting at number_1/number_2.
random int <number> to <number>:
    user.gdscript_random_int(number_1, number_2)

random float <user.number_prose_unprefixed_first> to <user.number_prose_unprefixed_second>:
    user.gdscript_random_float(number_prose_unprefixed_first, number_prose_unprefixed_second)

randomize seed:
    user.gdscript_randomize()

get node <user.text>:
    user.gdscript_get_node(text)

add child <user.text>:
    user.gdscript_add_child(text)

queue free:
    user.gdscript_queue_free()

is instance valid <user.text>:
    user.gdscript_is_instance_valid(text)

has node <user.text>:
    user.gdscript_has_node(text)

return:
    user.gdscript_return()

pass:
    user.gdscript_pass()

print <user.text>:
    user.gdscript_print(text)

class name <user.text>:
    user.gdscript_class_name(text)

extends <user.text>:
    user.gdscript_extends(text)

assert <user.text>:
    user.gdscript_assert(text)
