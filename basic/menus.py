import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Orders')
        panel = wx.Panel(self)
        self.create_menu()

        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, "Open File", "Open a folder with files"
        )

        menu_bar.Append(file_menu, '&File')

        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_file,
            source=open_folder_menu_item
        )
        self.SetMenuBar(menu_bar)

    def on_open_file(self):
        title = 'Pick a file'
        dlg = wx.DirDialog(self, title, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            print("Okay!")

        dlg.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
