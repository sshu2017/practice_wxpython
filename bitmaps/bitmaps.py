### add images to buttons
import wx

ID_BUTTON = 100
ID_EXIT = 200
ID_SPLITER = 300


# class MyListCtrl(wx.ListCtrl):
#     def __init__(self, parent):
#         wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)
#
#         images = ['img/guitar.png', 'img/soccer.png']
#
#         self.InsertColumn(0, 'Name')
#         self.InsertColumn(1, 'Ext')
#
#         self.SetColumnWidth(0, 300)
#         self.SetColumnWidth(1, 300)
#
#         self.il = wx.ImageList(16, 16)
#
#         for i in images:
#             self.il.Add(wx.Bitmap(i))
#
#         self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None)
        panel = wx.Panel(self)
        btn = wx.Button(panel, label='Ok')

        self.InitUI()
        self.Show()

    def InitUI(self):
        tb = self.CreateToolBar(wx.TB_VERTICAL | wx.NO_BORDER)
        tb.SetToolBitmapSize(wx.Size(10, 10))
        tb.AddTool(10, 'guitar', wx.Bitmap('img/guitar.png'))
        tb.AddSeparator()
        tb.AddTool(20, 'soccer', wx.Bitmap('img/soccer.png'), kind=wx.ITEM_CHECK)


def main():
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
