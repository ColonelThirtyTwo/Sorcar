import bpy

from bpy.props import StringProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode

class ScAddToCollection(Node, ScObjectOperatorNode):
    bl_idname = "ScAddToCollection"
    bl_label = "Add Object to Collection"

    in_name: StringProperty(default="", update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketString", "Name").init("in_name", True)
    
    def error_condition(self):
        return(
            super().error_condition()
            or self.inputs["Name"].default_value == ""
            or self.inputs["Name"].default_value not in bpy.data.collections
        )

    def functionality(self):
        collection = bpy.data.collections[self.inputs["Name"].default_value]
        obj = self.inputs["Object"].default_value
        if obj.name not in collection.objects:
            collection.objects.link(obj)
