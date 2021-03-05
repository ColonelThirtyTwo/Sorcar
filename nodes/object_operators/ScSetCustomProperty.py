import bpy

from bpy.types import Node
from bpy.props import StringProperty
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode
from ...helper import focus_on_object

class ScSetCustomProperty(Node, ScObjectOperatorNode):
    bl_idname = "ScSetCustomProperty"
    bl_label = "Set Custom Property"

    in_name: StringProperty(default="", update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketString", "Name").init("in_name", True)
        self.inputs.new("ScNodeSocketUniversal", "Value")
    
    def error_condition(self):
        return(
            super().error_condition()
            or self.inputs["Name"].default_value == ""
        )
    
    def functionality(self):
        obj = self.inputs["Object"].default_value
        obj[self.inputs["Name"].default_value] = self.inputs["Value"].default_value
