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

import bpy


class EmptyOperator(bpy.types.Operator):
    """Empty operator"""
    bl_idname = "object.empty_operator"
    bl_label = "Empty operator"
    bl_options = {'REGISTER', 'UNDO'}

    example_prop: bpy.props.BoolProperty(name="Example prop", default=False)

    @classmethod
    def poll(cls, context):
        return (context.space_data.type == 'VIEW_3D'
            and len(context.selected_objects) > 0
            and context.view_layer.objects.active
            and context.object.mode == 'OBJECT')

    def execute(self, context):
        self.report({'INFO'}, "Hello world!")
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)

classes = (
    EmptyOperator,
)

def menu_func(self, context):
    layout = self.layout
    layout.separator()

    layout.operator_context = "INVOKE_DEFAULT"
    layout.operator(EmptyOperator.bl_idname, text=EmptyOperator.bl_label)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)


if __name__ == "__main__":
    register()
