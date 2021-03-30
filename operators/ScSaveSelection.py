import bpy

from bpy.types import Operator
from ..helper import sc_poll_op


class ScSaveSelection(Operator):
    """Save the components of the mesh currently selected"""

    bl_idname = "sorcar.save_selection"
    bl_label = "Save Selection"

    @classmethod
    def poll(cls, context):
        return sc_poll_op(context)

    def execute(self, context):
        context.space_data.edit_tree.nodes.active.save_selection()
        return {"FINISHED"}
