import wx
import uuid

class FullProcess(wx.ScrolledCanvas):
    def __init__(self, parent, registry, *args, **kwds):
        self.parent = parent
        self._noderegistry = registry
        super().__init__()

    def _Init(self, idname):
        self.InitSockets()
        self.InitHeaderColor()
        self.SetIdName(idname)

    def AddUnit(self, idname, pos=(0, 0), location='POSITION'):
        node = self._noderegistry[idname](self, uuid.uuid4())
        node._Init(idname)

    def InitSockets(self):
        print(f"DEBUG - InitSockets")

    def InitHeaderColoer(self):
        print(f"DEBUG - InitHeaderColor")

    def SetIdName(self):
        print(f"DEBUG - SetIdName")


class ImageNode(NodeBase):
    def __init__(self, nodegraph, _id):
        super().__init__(self, nodegraph, _id)

        self._label = "Image"
        self._category = "INPUT"
        self._parameters = {
            "Image": None
        }