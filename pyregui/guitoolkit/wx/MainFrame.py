#!/usr/bin/env python

import wx, wx.lib.dialogs


class MainFrame(wx.Frame):
    
    def __init__(self, parent=None, id=-1, name = "hello", toolkit = None,
                 pos = wx.DefaultPosition,
                 logoimage = None, pyreapp = None, pyreapp_executable = None):
        self.logoimage = logoimage
        self.toolkit = toolkit
        self.pyreapp = pyreapp
        self.pyreapp_executable = pyreapp_executable
        #size = self.logoimage.GetWidth(), self.logoimage.GetHeight()
        wx.Frame.__init__(self, parent,id,name, pos, (600,200))
        print "MainFrame %s created" % name
        self.drawscreen()
        return


    def drawscreen(self):
        self.sizer = wx.BoxSizer( wx.HORIZONTAL )
        self.createPanel()
        self.sizer.Add( self.panel, 0, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show(True)
        return


    def createPanel(self):
        self.panel = self.toolkit.MainPanel( 
            self, toolkit = self.toolkit, pyreapp = self.pyreapp,
            pyreapp_executable = self.pyreapp_executable,
            logoimage = self.logoimage)
        return

    pass # end of MainFrame


class MainPanel(wx.Panel):


    def __init__(self, parent,
                 toolkit = None, pyreapp = None,
                 pyreapp_executable = None, logoimage = None):
        self.toolkit = toolkit; self.pyreapp = pyreapp
        self.pyreapp_executable = pyreapp_executable

        wx.Panel.__init__(self, parent, -1)
        hbox = wx.BoxSizer( wx.HORIZONTAL )

        if logoimage:
            logoimage = logoimage.ConvertToBitmap()
            self.launcherButton = wx.BitmapButton(self, -1, logoimage, pos = (200, 150))
        else:
            self.launcherButton = wx.Button(self, -1, "Pyre app launcher")
            pass
        
        self.launcherButton.SetToolTipString('configure launcher')
        
        self.Bind(wx.EVT_BUTTON, self.OnLauncherOptions, self.launcherButton)
        
        hbox.Add( self.launcherButton, 0, wx.ALIGN_TOP, 20)
        

        hbox.Add( wx.BoxSizer(), 0, wx.ALIGN_CENTER, 20) #spacer

        rightColumn = wx.BoxSizer(wx.VERTICAL)
        col1row0 = wx.BoxSizer()
        topLbl = wx.StaticText( self, -1, self.pyreapp.name)
        topLbl.SetFont( wx.Font(28, wx.SWISS, wx.NORMAL, wx.BOLD ) )
        col1row0.Add( topLbl, 0, wx.ALIGN_CENTER)
        rightColumn.Add(col1row0,0, wx.ALIGN_CENTER)

        # docstr inside a scrolled panel
        docBox = self.createDocBox()

        rightColumn.Add(docBox, 1, wx.ALIGN_CENTER, 20)
        
        #rightColumn.Add(wx.StaticLine(self, -1, size=(300,1)), 1, wx.ALIGN_CENTER, 5)
        rightColumn.AddSpacer( (300,40) )

        bottom_box = wx.BoxSizer(wx.HORIZONTAL)
        self.inventoryButton = wx.Button(self, -1, "Configure")
        self.Bind(wx.EVT_BUTTON, self.OnAppInventory, self.inventoryButton )
        bottom_box.Add( self.inventoryButton, 0, wx.ALIGN_LEFT )

        bottom_box.AddSpacer( (10,10) )
        
        self.saveInvButton = wx.Button(self, -1, "Save configuration")
        self.Bind(wx.EVT_BUTTON, self.OnSaveInventory, self.saveInvButton )
        bottom_box.Add( self.saveInvButton, 0, wx.ALIGN_LEFT )

        bottom_box.Add( wx.BoxSizer(), 1 )

        self.runButton = wx.Button(self, -1, "Run")
        self.runButton.SetToolTipString('Run Pyre Application: %s' % self.pyreapp.name)
        self.Bind(wx.EVT_BUTTON, self.OnRun, self.runButton )
        bottom_box.Add( self.runButton, 0, wx.ALIGN_RIGHT )

        bottom_box.AddSpacer( (10,10) )

        self.exitButton = wx.Button(self, -1, "Exit")
        self.Bind(wx.EVT_BUTTON, self.OnExitButton, self.exitButton )
        bottom_box.Add( self.exitButton, 0, wx.ALIGN_RIGHT )

        rightColumn.Add(bottom_box, 1, wx.GROW, 5)
        hbox.Add( rightColumn, 1 )

        border = wx.BoxSizer()

        border.Add(hbox, 1, wx.GROW|wx.ALL, 25)
        border.Fit(self)
        self.SetSizer(border)
        self.Layout()
        self._createLauncher()
        return


    def createDocBox(self):
        from MainFrameDocBox import MainFrameDocBox
        docBox = MainFrameDocBox( self, self.pyreapp, size=(480,100) )
        return docBox


    def OnRun(self, evt):
        self._saveConfiguration()
        self._saveLauncherConfiguration()
        launcherApp = self.launcherApp
        try:
            launcherApp.run( self.pyreapp_executable )
            m = "%s done successfully" % self.pyreapp_executable
        except Exception, err:
            import traceback
            m = traceback.format_exc()
            pass
        wx.MessageBox( m, "" )
        return


    def OnExitButton(self, evt):
        self.GetParent().Close()
        return


    def OnAppInventory(self, event):
        return self.toolkit.InventoryDialogLoop( self, self.pyreapp, self.toolkit )


    def OnSaveInventory(self, event):
        import os
        if self.__dict__.get("defaultDir") is None: 
          try: self.defaultDir = os.environ['PWD']
          except: self.defaultDir = os.curdir
          pass
        if self.__dict__.get("defaultFile") is None: self.defaultFile = "%s.pml" % self.pyreapp.name

        path = wx.FileSelector(
            message = "Save configurations",
            default_path = self.defaultDir,
            default_filename = self.defaultFile,
            wildcard = "*.pml",
            flags = wx.SAVE, )
        if path:
            abspath = os.path.abspath( path )
            dir, fn = os.path.split( abspath )
            self.defaultDir = dir
            self.defaultFile = fn
            self._saveConfiguration( abspath )
            pass
        return
    

    def OnLauncherOptions(self, event):
        return self.toolkit.InventoryDialogLoop( self, self.launcherApp, self.toolkit )


    def OnHelpButton(self, docstr, title="Pyre Docstring"):
        def _(event): 
            dlg = wx.lib.dialogs.ScrolledMessageDialog(self, docstr, title)
            dlg.ShowModal()
        return _


    def _createLauncher(self):
        from pyregui.LauncherApp import LauncherApp
        self.launcherApp = LauncherApp()
        self.launcherApp.run()
        return


    def _saveConfiguration(self, path = None):
        saveConfiguration( self.pyreapp, path )
        return
    

    def _saveLauncherConfiguration(self, path = None):
        saveConfiguration( self.launcherApp, path )
        return


    pass # end of MainPanel



def saveConfiguration( pyreapp, path = None ):
    from pyregui.inventory.configurationSaver import toPml
    name = pyreapp.name
    filename = "%s.pml" % name
    from os.path import join
    if path : filename = path
    toPml( pyreapp, filename )
    return

# end of file
