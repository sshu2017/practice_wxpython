import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
             title="My Frame",
             size=(300, 300))
        panel = wx.Panel()
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "Pos: ", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue(f"{pos.x}, {pos.y}")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
