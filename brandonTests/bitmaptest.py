import wx

class TestPanel(wx.Panel):
    
    
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)
        self.log = log

        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, -1, "bitmap test")
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        fgs = wx.FlexGridSizer(0, 3, 10, 10)

#        combo = wx.ComboBox(self, -1, "", choices = ArtClients,
#                           style = wx.CB_DROPDOWN|wx.CB_READONLY)
#        fgs.Add(combo, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        self.Bind(wx.EVT_COMBOBOX, self.OnSelectClient, combo)
#        combo.Select(0)
#
#        combo = wx.ComboBox(self, -1, "", choices = ArtIDs,
#                           style = wx.CB_DROPDOWN|wx.CB_READONLY)
#        fgs.Add(combo, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        self.Bind(wx.EVT_COMBOBOX, self.OnSelectID, combo)
#        combo.Select(0)
#
#        cb = wx.CheckBox(self, -1, "Use custom provider")
#        fgs.Add(cb, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        self.Bind(wx.EVT_CHECKBOX, self.OnUseCustom, cb)
#
#        fgs.Add((10, 10), 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        fgs.Add((10, 10), 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        fgs.Add((10, 10), 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.VERTICAL)
        #bmp = wx.EmptyBitmap(16,16)
        prefix='/home/jbk/DANSE/pyregui/resources/icons/'
        bmp = wx.Bitmap(prefix+'pyre.xbm')
        self.bmp16 = wx.StaticBitmap(self, -1, bmp)
        box.Add(self.bmp16, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        text = wx.StaticText(self, -1, "16x16")
        box.Add(text, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        fgs.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

#        box = wx.BoxSizer(wx.VERTICAL)
#        bmp = wx.EmptyBitmap(32,32)
#        self.bmp32 = wx.StaticBitmap(self, -1, bmp)
#        box.Add(self.bmp32, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        text = wx.StaticText(self, -1, "32x32")
#        box.Add(text, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#
#        fgs.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#
#        box = wx.BoxSizer(wx.VERTICAL)
#        bmp = wx.EmptyBitmap(48,48)
#        self.bmp48 = wx.StaticBitmap(self, -1, bmp)
#        box.Add(self.bmp48, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#        text = wx.StaticText(self, -1, "48x48")
#        box.Add(text, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#
#        fgs.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(fgs, 0, wx.ALL, 5)
        self.SetSizer(sizer)



if __name__ == "__main__":
#    demo_plotter(sample_graph())
    
    # Make a frame to show it
    import sys
    app = wx.PySimpleApp()
    frame = wx.Frame(None)
    tp = TestPanel(frame, sys.stdout)
    #frame = wx.Frame(None,-1,'Plottables')
    #plotter = Plotter(frame)
    frame.Show()
    app.MainLoop()