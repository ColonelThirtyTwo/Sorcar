import bpy

from bpy.props import EnumProperty, BoolProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode

class ScSetObjectVisible(Node, ScObjectOperatorNode):
    bl_idname = "ScSetObjectVisible"
    bl_label = "Set Object Visibility"

    in_type: EnumProperty(items=[
        ('VIEWPORT', 'Viewport', ''),
        ('RENDER', 'Render', ''),
        ('SELECT', 'Selection', ''),
    ], default='VIEWPORT', update=ScNode.update_value)
    in_set: BoolProperty(update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketString", "Type").init("in_type", True)
        self.inputs.new("ScNodeSocketBool", "Is Visible").init("in_set", True)

    def error_condition(self):
        return(
            super().error_condition()
            or (not self.inputs["Type"].default_value in ['VIEWPORT', 'RENDER', 'SELECT'])
        )

    def functionality(self):
        typ = self.inputs["Type"].default_value
        obj = self.inputs["Object"].default_value
        visible = self.inputs["Is Visible"].default_value
        if typ == "VIEWPORT":
            obj.hide_viewport = not visible
        elif typ == "SELECT":
            obj.hide_select = not visible
        elif typ == "RENDER":
            obj.hide_render = not visible
        else:
            assert False
