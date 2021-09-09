import wx
import sys


class Frame(wx.Frame):
    def __init__(self):
        print("Frame __init__")
        super().__init__(parent=None, id=1, title="hello redirect")


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print("App __init__")
        super(App, self).__init__(self, redirect, filename)

    def OnInit(self):
        print("OnInit")
        self.frame = Frame(parent=None, id=-1, title='startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretended error message", file=sys.stderr)
        return True

    def OnExit(self):
        print("OnExit")


if __name__ == '__main__':
    app = App()
    print("Before MainLoop")
    app.MainLoop()
    print("After MainLoop")