import wx
import sys
import platform
from full_process import FullProcess


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, id=wx.ID_ANY,
                         title='App1', size=wx.Size(200, 200))
        registry = {
            '1': 1,
            '2': 2
        }
        process = FullProcess(parent="1", registry=registry)
        print(f"DEBUG - process={process}")
        process.AddUnit(idname='1', pos=(100, 200))



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Maximize()
    frame.Show()
    app.MainLoop()
