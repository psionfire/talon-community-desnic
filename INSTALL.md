# Installation Guide for Talon Godot Support

## Prerequisites
- Talon Voice installed on the system.
- Godot Engine installed (version 4+).
- Optional: Visual Studio Code if editing scripts outside of Godot.

## Installation
1. Clone this repository (or download as ZIP) into the Talon user directory:
   - Windows: %APPDATA%\Talon\user
   - macOS: ~/.talon/user
   - Linux: ~/.talon/user
2. Ensure the folder is named something recognizable like `talon-godot-support`.

## Usage
1. Open Godot and/or VSCode.
2. Voice commands in `.gd` files will trigger GDScript snippets.
3. Voice commands while the Godot editor is active will trigger editor shortcuts.

## Examples
- Say: "function jump" → inserts:
  ```gdscript
  func jump():
  ```
- Say: "signal health changed" → inserts:
  ```gdscript
  signal health_changed
  ```
- Say: "play scene" → triggers F6 in Godot editor.

## Updating
- Pull latest changes from GitHub if updates are released.
- Restart Talon after updates.

## Notes
- Default Godot shortcuts are assumed (from the Godot documentation).
- If shortcuts are customized in Godot, update the corresponding `.talon` files.

After installation, follow the [Testing guide](lang/gdscript/TESTING.md) to verify GDScript and Godot support.
