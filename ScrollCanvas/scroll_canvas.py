import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Canvas")

        sw = wx.ScrolledCanvas(self)

        bmp = wx.Image('wxPyWiki.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.StaticBitmap(sw, -1, bmp)

        sw.SetScrollbars(20, 20, 55, 40)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Show()

    def OnClose(self, event):
        self.Destroy()
        wx.Exit()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()