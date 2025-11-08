import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Sizer Sample", size=(400, 200))
        panel = wx.Panel(self)

        # === ウィジェット ===
        self.text = wx.StaticText(panel, label="こんにちは！", style=wx.ALIGN_CENTER)
        self.button = wx.Button(panel, label="押してみる")

        # === レイアウト ===
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        vbox.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        panel.SetSizer(vbox)

        # イベント
        self.button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        self.text.SetLabel("ボタンが押されました！")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
