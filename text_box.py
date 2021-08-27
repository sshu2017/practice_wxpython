import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Text Box')

        # create menu
        self.create_menu()

        # set window initial size
        self.SetSize(wx.Size(800, 200))

        # display window
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_file_menu_item = file_menu.Append(
            wx.ID_ANY, "Open File"
        )
        save_file_menu_item = file_menu.Append(
            wx.ID_ANY, "Save File"
        )
        quit_item = file_menu.Append(
            wx.ID_ANY, "Quit"
        )


        about_menu = wx.Menu()
        about_menu_item = about_menu.Append(
            wx.ID_ABOUT, "About PoopyLab"
        )

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(about_menu, "&About")

        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_file,
            source=open_file_menu_item
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_save_file,
            source=save_file_menu_item
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_quit,
            source=quit_item
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_about,
            source=about_menu_item
        )

        self.SetMenuBar(menu_bar)

    def on_open_file(self, event):
        title = 'Open a file'
        print(f"DEBUG title = {title}")
        dlg = wx.FileDialog(self, title, style=wx.DD_DEFAULT_STYLE)

        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            print(f"DEBUG dirname = {filename}")
            # read file
            with open(filename, 'r') as f:
                self.text_contents = f.read()

        wx.StaticText(self, label=self.text_contents)

    def on_about(self, event):
        print("clicked about")
        pass

    def on_save_file(self, event):
        print("clicked save file")
        pass

    def on_quit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
