#!/usr/bin/env python

import wx, os


class MainWindowApp(wx.PySimpleApp):


    def __init__(self, pyreapp, pyreapp_executable,  toolkit, *args, **kwargs):
        self.toolkit = toolkit
        buttonfile = self._buttonfile()
        if not (os.path.exists(buttonfile) and os.path.isfile(buttonfile)):
            raise "Cannot find button image file %s" % buttonfile
        self.buttonfile = buttonfile
        
        self.pyreapp = pyreapp
        self.pyreapp_executable = pyreapp_executable
        wx.PySimpleApp.__init__(self, *args, **kwargs)

        return
    

    def OnInit(self):
        #there is a 64-bit bug with wx.Image
        #(2.8.4.2). We better make sure we can deal with case
        #where we cannot display logo.
        try:
            image = wx.Image(self.buttonfile, wx.BITMAP_TYPE_PNG)
        except:
            image = None
            pass
        MainFrame = self.toolkit.MainFrame
        self.frame = MainFrame(None, -1, self.pyreapp.name, self.toolkit,
                               logoimage = image, pyreapp = self.pyreapp,
                               pyreapp_executable = self.pyreapp_executable)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
##         self.frame = wx.Frame( None, -1, "hello" )
##         self.frame.Show(True)
        return True


    def _buttonfile(self):
        from pyregui.paths import resources
        return os.path.join( resources,"icons", 'pyre.png')


# $Id: MainWindowApp.py,v 1.1 2006/08/09 23:09:22 linjiao Exp $
# end of file
