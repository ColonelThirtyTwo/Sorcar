import bpy

from .._base.node_base import ScNode
from ...helper import focus_on_object


class ScDeletionNode(ScNode):
    def init(self, context):
        self.node_executable = True
        super().init(context)
        self.inputs.new("ScNodeSocketObject", "Object")
        self.outputs.new("ScNodeSocketObject", "Object")

    def error_condition(self):
        return self.inputs["Object"].default_value == None

    def pre_execute(self):
        focus_on_object(self.inputs["Object"].default_value, True)

    def post_execute(self):
        return {"Object": self.inputs["Object"].default_value}
