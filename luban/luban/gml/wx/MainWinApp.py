#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx




WxPyAppBase = wx.PySimpleApp
#WxPyAppBase = wx.PyApp


class MainWinApp(WxPyAppBase):

    def __init__(self,  name):
        self.name = name
        WxPyAppBase.__init__(self)
        #self.SetAssertMode( wx.PYAPP_ASSERT_DIALOG )
        return


    def start(self):
        """start the application"""
        #this should be called after the main frame is set
        # i.e., self.frame must be an instance of MainFrame
        # this is automatically done in the WxRenderer
        self.frame.Show(True) 
        self.MainLoop()
        return


    def end(self):
        self.frame.Close()
        return
    

    def OnInit(self):
        return True


# version
__id__ = "$Id$"

# End of file 
