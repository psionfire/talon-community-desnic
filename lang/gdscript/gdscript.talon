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
    insert("extends ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

state class name <user.text>:
    insert("class_name ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

signal <user.text>:
    insert("signal ")
    insert(user.formatted_text(text, "SNAKE_CASE"))

state on ready (var | variable) <user.text>:
    insert("@onready var ")
    user.code_public_variable_formatter(text)
