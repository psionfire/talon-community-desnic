# Testing Godot and GDScript Support
This checklist covers only the Godot editor commands and GDScript language snippets added in this fork. For other languages (Python, C#, etc.), refer to the upstream community repo.

## GDScript Commands
- `function jump` → `func jump():`
- `private function update` → `func _update():`
- `variable health int` → `var health: int`
- `export int speed` → `@export var speed: int`
- `signal pressed` → `signal pressed`
- `emit signal pressed` → `emit_signal("pressed")`
- `on signal pressed` → `func _on_pressed(): pass`
- `enum state idle running jumping` → `enum State { IDLE, RUNNING, JUMPING }`
- `random int one to ten` → `randi_range(1, 10)`
- `enter tree` → `func _enter_tree():`

## Godot Editor Commands
- `play project` → F5
- `play scene` → F6
- `pause scene` → F7
- `stop scene` → F8
- `add node` → Ctrl+A
- `duplicate node` → Ctrl+D
- `delete node` → Delete
- `save scene` → Ctrl+S
- `undo` → Ctrl+Z
- `redo` → Ctrl+Shift+Z
- `toggle output` → F12
- `toggle debugger` → Shift+F12
- `switch to 2D` → F1
- `switch to 3D` → F2
- `zoom in` → Ctrl+Plus
- `zoom out` → Ctrl+Minus
- `reset zoom` → Ctrl+0
