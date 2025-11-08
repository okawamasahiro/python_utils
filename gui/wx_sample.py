import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="wxPython Sample", size=(300, 200))
        panel = wx.Panel(self)

        # テキスト
        self.label = wx.StaticText(panel, label="Hello wxPython!", pos=(20, 20))

        # ボタン
        button = wx.Button(panel, label="クリック", pos=(20, 60))
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        self.label.SetLabel("ボタンが押されました！")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()