bl_info = {
    "name": "maze generator",
    "category": "Object",
}

import bpy
import maze_generator

class propertySettings(bpy.types.PropertyGroup):
    bpy.types.Scene.maze_size= bpy.props.IntProperty(name ="Maze size", min=3, default = 11)

class mazeGen(bpy.types.Operator):
    """My Object Moving Script"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.maze_generate"        # unique identifier for buttons and menu items to reference.
    bl_label = "Generate maze"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        # The original script
        maze_generator.size = bpy.context.scene.maze_size
        maze_generator.generate_maze()

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

class mazePanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_maze_panel"
    bl_label = "Maze"
    bl_space_type = 'VIEW_3D'
    #bl_region_type = 'WINDOW'
    bl_region_type = 'TOOLS'
    #bl_context = "render"
    bl_category = "Create"

    def draw(self, context):
        self.layout.operator("object.maze_generate", icon='MESH_CUBE', text="Generate maze")
        row = self.layout.row()
        row.prop(bpy.context.scene, "maze_size")

def register():
    bpy.utils.register_class(propertySettings)
    bpy.utils.register_class(mazeGen)
    bpy.utils.register_class(mazePanel)


def unregister():
    bpy.utils.unregister_class(propertySettings)
    bpy.utils.unregister_class(mazeGen)
    bpy.utils.unregister_class(mazePanel)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
