#Boa:Dialog:Dialog1

import wx
import wx.grid

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1GRID1, wxID_DIALOG1PANEL1, wxID_DIALOG1STATICTEXT1, 
 wxID_DIALOG1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Dialog1(wx.Dialog):
    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(503, 218), size=wx.Size(1280, 733),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(1280, 733))

        self.panel1 = wx.Panel(id=wxID_DIALOG1PANEL1, name='panel1',
              parent=self, pos=wx.Point(8, 0), size=wx.Size(1264, 720),
              style=wx.TAB_TRAVERSAL)

        self.grid1 = wx.grid.Grid(id=wxID_DIALOG1GRID1, name='grid1',
              parent=self.panel1, pos=wx.Point(16, 160), size=wx.Size(816, 552),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(8, 16), size=wx.Size(69, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(88, 8), size=wx.Size(80, 27),
              style=0, value='textCtrl1')

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.table = TwoAtomPotentialTable()
        self.grid1.SetTable(self.table)
        self.setGridConditions()
        gridlib.EVT_GRID_CELL_LEFT_DCLICK(self, self.OnLeftDClick)
        gridlib.EVT_GRID_CELL_CHANGE(self, self.OnCellChange)
        #self.Bind(gridlib.EVT_GRID_CELL_CHANGE, self.OnCellChange)
        
    def setGridConditions(self):
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)
        self.SetMargins(0,0)
        self.AutoSizeColumns(True)
        self.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
