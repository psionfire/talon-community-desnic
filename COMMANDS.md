# Godot and GDScript Voice Command Cheatsheet

## GDScript Language Commands

### Class Structure and Signals
- `state class name player controller` → `class_name PlayerController`
- `class name player controller` → `class_name PlayerController`
- `state extends character body two d` → `extends CharacterBody2D`
- `extends character body two d` → `extends CharacterBody2D`
- `signal pressed` → `signal pressed`
- `emit signal pressed` → `emit_signal("pressed")`
- `connect signal pressed` → `.connect("pressed", self, "_on_pressed")`
- `on signal pressed` → `func _on_pressed(): pass`

### Functions and Parameters
- `function jump` → `func jump():`
- `private function update` → `func _update():`
- `static function initialize` → `static func initialize():`
- `private static function helper` → `static func _helper():`
- `parameter target` → `(target)`
- `parameter target vector two` → `(target: Vector2)`
- `return type vector three` → `-> Vector3`

### Variables and Constants
- `variable health` → `var health`
- `variable health int` → `var health: int`
- `variable score float` → `var score: float`
- `state on ready var/variable camera` → `@onready var camera`
- `onready var camera` → `@onready var camera`
- `export int speed` → `@export var speed: int`
- `export float speed` → `@export var speed: float`
- `export bool active` → `@export var active: bool`
- `export speed` → `@export var speed`
- `const max speed = 300` → `const MAX_SPEED = 300`

### Flow Control and Structure
- `if health less than one` → `if health less than one:`
- `elif health less than five` → `elif health less than five:`
- `else` → `else:`
- `match state` → `match state:`
- `for enemy in enemies` → `for enemy in enemies:`
- `for index in range ten` → `for index in range(10):`
- `while running` → `while running:`
- `pass` → `pass`
- `return` → `return`

### Lifecycle and Input Callbacks
- `init` → `func _init():`
- `ready` → `func _ready():`
- `enter tree` → `func _enter_tree():`
- `exit tree` → `func _exit_tree():`
- `process` → `func _process(delta):`
- `physics process` → `func _physics_process(delta):`
- `input event` → `func _input(event):`
- `unhandled input event` → `func _unhandled_input(event):`

### Collections and Data
- `empty array` → `[]`
- `array enemies` → `[enemies]`
- `empty dictionary` → `{}`
- `dictionary health: 100` → `{health: 100}`
- `enum state idle running jumping` → `enum State { IDLE, RUNNING, JUMPING }`

### Expressions and Utility
- `set health equals zero` → `health = 0`
- `increment score` → `score += 1`
- `decrement lives` → `lives -= 1`
- `random int one to ten` → `randi_range(1, 10)`
- `random float zero point five to two` → `randf_range(0.5, 2)`
- `randomize seed` → `randomize()`
- `get node player` → `get_node("player")`
- `add child enemy` → `add_child(enemy)`
- `queue free` → `queue_free()`
- `is instance valid player` → `is_instance_valid(player)`
- `has node player` → `has_node("player")`
- `print score` → `print(score)`
- `assert ready` → `assert(ready)`

## Godot Editor Commands

### Playback and Debugging
- `play project` → F5
- `play scene` → F6
- `pause scene` → F7
- `stop scene` → F8
- `play custom scene` → F9

### Scene Tree Editing
- `add node` → Ctrl+A
- `duplicate node` → Ctrl+D
- `delete node` → Delete
- `rename node` → F2
- `move node up` → Ctrl+Up
- `move node down` → Ctrl+Down

### File and Edit Actions
- `save scene` → Ctrl+S
- `undo` → Ctrl+Z
- `redo` → Ctrl+Shift+Z
- `copy` → Ctrl+C
- `cut` → Ctrl+X
- `paste` → Ctrl+V
- `find in files` → Ctrl+Shift+F

### Interface Toggles
- `toggle output` → F12
- `toggle debugger` → Shift+F12
- `toggle animation` → Ctrl+F12
- `toggle audio` → Alt+F12
- `toggle import` → Ctrl+Shift+F12

### Workspace Navigation
- `focus script editor` → F11
- `switch to 2d` → F1
- `switch to 3d` → F2
- `switch to script` → F3
- `switch to assetlib` → F4

### View Management
- `zoom in` → Ctrl+Plus
- `zoom out` → Ctrl+Minus
- `reset zoom` → Ctrl+0

### File Browsing
- `search files` → Alt+Shift+O
- `quick open scene` → Ctrl+Shift+O
