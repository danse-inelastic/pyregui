#Boa:Frame:Frame2

import wx
import addEditDialog

potentialDataObject=['potential1','potential2']

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2ADD, wxID_FRAME2EDIT, wxID_FRAME2listBox, 
 wxID_FRAME2REMOVE, wxID_FRAME2SPLITTERWINDOW1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame2(wx.Frame):
    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(480, 275), size=wx.Size(1280, 733),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        self.SetClientSize(wx.Size(1280, 733))

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_FRAME2SPLITTERWINDOW1,
              name='splitterWindow1', parent=self, point=wx.Point(0, 0),
              size=wx.Size(200, 100), style=wx.SP_3D)

        self.listBox = wx.ListBox(choices=[], id=wxID_FRAME2listBox,
              name='listBox', parent=self.splitterWindow1, pos=wx.Point(24,
              32), size=wx.Size(552, 664), style=0)
        self.listBox.Bind(wx.EVT_LISTBOX, self.OnlistBoxListbox,
              id=wxID_FRAME2listBox)

        self.add = wx.Button(id=wxID_FRAME2ADD, label=u'add', name=u'add',
              parent=self.splitterWindow1, pos=wx.Point(648, 40),
              size=wx.Size(85, 32), style=0)
        self.add.Bind(wx.EVT_BUTTON, self.OnAdd, id=wxID_FRAME2ADD)

        self.edit = wx.Button(id=wxID_FRAME2EDIT, label=u'edit', name=u'edit',
              parent=self.splitterWindow1, pos=wx.Point(648, 80),
              size=wx.Size(85, 32), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_FRAME2EDIT)

        self.remove = wx.Button(id=wxID_FRAME2REMOVE, label=u'remove',
              name=u'remove', parent=self.splitterWindow1, pos=wx.Point(648,
              120), size=wx.Size(85, 32), style=0)
        self.remove.Bind(wx.EVT_BUTTON, self.OnRemoveButton,
              id=wxID_FRAME2REMOVE)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        #list box settings
        self.SetTitle("Potential List")
        self.selectedItems = None
        #add some items to the list
        for pot in potentialDataObject:
            self.listBox.Append(pot)

    def OnlistBoxListbox(self, event):
        self.selectedItems=self.listBox.GetSelections()

    def OnAdd(self, event):
        dlg = addEditDialog.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnEditButton(self, event):
        dlg = addEditDialog.Dialog1(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnRemoveButton(self, event):
        for i in self.selectedItems:
            self.listBox.Delete(i)
