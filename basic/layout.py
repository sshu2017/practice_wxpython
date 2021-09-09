import wx


app = wx.App()
window = wx.Frame(None, title="Frame", size=(500, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
window.Show(True)
app.MainLoop()