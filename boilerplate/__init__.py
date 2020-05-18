bl_info = {
    "name": "Addon boilerplate",
    "author": "Artem Poletsky",
    "version": (1, 0, 0),
    "blender": (2, 82, 0),
    "location": "Object",
    "description": "For quick start new addon development",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

if "bpy" in locals():
    import importlib
    importlib.reload(preferences)
    importlib.reload(empty_operator)
    EmptyOperator = empty_operator.EmptyOperator

else:
    from . import preferences
    from .empty_operator import EmptyOperator

import bpy

classes = (
    preferences.BoilerplatePreferences,
    preferences.BoilerplatePreferencesAddKeymapOperator,
    EmptyOperator
)

def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator_context = "INVOKE_DEFAULT"
    layout.operator(EmptyOperator.bl_idname, text = EmptyOperator.bl_label)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    preferences.register_keymaps()
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)

    preferences.unregister_keymaps()

if __name__ == "__main__":
    register()
