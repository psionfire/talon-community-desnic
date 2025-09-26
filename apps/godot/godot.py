from talon import Context, Module

mod = Module()
mod.apps.godot = "app.name: Godot"
mod.apps.godot = "app.name: Godot Engine"
mod.apps.godot = r"""
os: mac
and app.bundle: org.godotengine.godot
"""
mod.apps.godot = r"""
os: mac
and app.bundle: io.godotengine.godot
"""
mod.apps.godot = r"""
os: linux
and app.name: Godot
"""
mod.apps.godot = r"""
os: linux
and app.name: Godot Engine
"""
mod.apps.godot = r"""
os: windows
and app.exe: /godot.*\.exe/i
"""
mod.apps.godot = r"""
os: windows
and app.name: Godot Engine
"""

ctx = Context()
ctx.matches = r"""
app: godot
"""

lang_ctx = Context()
lang_ctx.matches = r"""
app: godot
not tag: user.code_language_forced
win.title: /(?i)(\.gd|godot engine)/
"""


@lang_ctx.action_class("code")
class CodeActions:
    def language():
        return "gdscript"
