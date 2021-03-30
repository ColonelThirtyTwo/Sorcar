import bpy

from bpy.props import StringProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode


class ScRemoveFromAllCollections(Node, ScObjectOperatorNode):
    bl_idname = "ScRemoveFromAllCollections"
    bl_label = "Remove Object from All Collection"

    def init(self, context):
        super().init(context)

    def functionality(self):
        obj = self.inputs["Object"].default_value
        for collection in obj.users_collection:
            collection.objects.unlink(obj)
