from ..umog_node import *
from ...engine import types, engine
import bpy

class NegateNode(UMOGNode):
    bl_idname = "umog_NegateNode"
    bl_label = "Negate Node"

    def init(self, context):
        self.inputs.new("FloatSocketType", "in")
        self.outputs.new("FloatSocketType", "out")
        super().init(context)

    def get_operation(self):
        return engine.Operation(
            engine.NEGATE,
            [types.Scalar()],
            [types.Scalar()],
            [],
            [engine.Argument(engine.ArgumentType.SOCKET, 0)])

    def update(self):
        pass