# GDScript and Godot Support

## Overview
This package ships Talon voice command support for Godot projects. Code-related commands live in [`lang/gdscript`](./), while Godot editor automation sits in [`apps/godot`](../../apps/godot/). Use both folders together to script game logic in GDScript and drive the editor UI hands-free.

## GDScript command coverage
The GDScript grammar exposes the following groups of commands:

- **Functions and methods** – create public, private, and static functions, add return types, and insert parameters via helpers such as `code_public_function`, `code_private_function`, and `gdscript_insert_parameter`.
- **Variables and constants** – declare standard, typed, exported, on-ready, and constant values using helpers like `gdscript_insert_variable`, `gdscript_insert_typed_variable`, `gdscript_insert_export`, `gdscript_insert_onready`, and `gdscript_insert_constant`.
- **Signals** – generate `signal` declarations, emitters, connection calls, and handler stubs (`gdscript_insert_signal`, `gdscript_emit_signal`, `gdscript_connect_signal`, `gdscript_on_signal`).
- **Control flow** – insert conditionals, matches, and loop constructs (`gdscript_insert_if`, `gdscript_insert_match`, `gdscript_insert_for`, `gdscript_insert_for_range`, `gdscript_insert_while`).
- **Lifecycle callbacks** – scaffold `_init`, `_ready`, `_enter_tree`, `_exit_tree`, `_process`, `_physics_process`, and input handlers through `gdscript_insert_lifecycle`, `gdscript_insert_process`, `gdscript_insert_physics_process`, and `gdscript_insert_input`.
- **Random helpers** – drop in `randomize`, `randi_range`, and `randf_range` calls with `gdscript_randomize`, `gdscript_random_int`, and `gdscript_random_float`.
- **Enums** – create typed enumerations via `gdscript_insert_enum`.
- **Arrays and dictionaries** – produce empty or pre-populated array/dictionary literals with `gdscript_insert_array` and `gdscript_insert_dictionary`.
- **Scene helpers** – insert `get_node`, `add_child`, `queue_free`, `is_instance_valid`, and `has_node` snippets with dedicated actions.
- **Operators** – leverage the shared `Operators` table for array subscripts, assignment, bitwise, and math operators (`code_get_operators`).

Additional utilities include keyword insertion (`gdscript_return`, `gdscript_pass`, `gdscript_print`, `gdscript_assert`), object setup (`gdscript_extends`, `gdscript_class_name`), and assignment helpers (`gdscript_assignment`, `gdscript_increment`, `gdscript_decrement`).

## Godot editor commands
[`apps/godot/godot.talon`](../../apps/godot/godot.talon) provides Talon shortcuts for common Godot editor workflows, grouped as follows:

- **Running and debugging** – play the project or current scene, pause, stop, and launch custom scenes.
- **Scene tree management** – add, duplicate, delete, rename, and reorder nodes.
- **Editing and undo** – save scenes, undo/redo, and cut/copy/paste content.
- **Panel toggles** – show and hide Output, Debugger, Animation, Audio, and Import panes.
- **Workspace navigation** – jump between Script, 2D, 3D, and Asset Library workspaces and focus the script editor.
- **Viewport zoom** – adjust editor zoom levels.
- **File system access** – search files and open scenes quickly.

## Voice command examples
A few representative examples illustrate how spoken phrases expand into GDScript:

| Voice command | Output |
| --- | --- |
| `"function move player"` | `func move_player():` |
| `"signal player hit"` | `signal player_hit` |
| `"for enemy in range ten"` | `for enemy in range(10):` |

## Extending the commands
To add new language snippets:

1. Implement the behavior in [`lang/gdscript/gdscript.py`](./gdscript.py) by adding a new `actions.user` method or extending existing helpers.
2. Map a spoken phrase to the action in [`lang/gdscript/gdscript.talon`](./gdscript.talon).
3. If the command requires supporting vocabulary (types, keywords, common functions), update the relevant `.talon-list` files in the same directory.
4. Test the command in Talon, ensuring it formats names according to the configured formatters.

For additional editor shortcuts, follow the same pattern inside [`apps/godot/godot.talon`](../../apps/godot/godot.talon), binding new phrases to key presses.
