import bpy

from bpy.props import PointerProperty, StringProperty
from bpy.types import Node
from .._base.node_base import ScNode


class ScGetVariable(Node, ScNode):
    bl_idname = "ScGetVariable"
    bl_label = "Get Variable"

    prop_nodetree: PointerProperty(
        name="NodeTree", type=bpy.types.NodeTree, update=ScNode.update_value
    )
    in_name: StringProperty(default="Var", update=ScNode.update_value)
    in_default: StringProperty(default="Value", update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketString", "Name").init("in_name", True)
        self.inputs.new("ScNodeSocketString", "Default").init("in_default")
        self.outputs.new("ScNodeSocketUniversal", "Value")

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, "prop_nodetree")

    def error_condition(self):
        return self.prop_nodetree == None or self.inputs["Name"].default_value == ""

    def pre_execute(self):
        if not hasattr(self.prop_nodetree, "variables"):
            self.prop_nodetree.variables = {}

    def functionality(self):
        if not self.inputs["Name"].default_value in self.prop_nodetree.variables:
            self.prop_nodetree.variables[
                self.inputs["Name"].default_value
            ] = self.inputs["Default"].default_value

    def post_execute(self):
        out = {}
        out["Value"] = self.prop_nodetree.variables[self.inputs["Name"].default_value]
        return out
