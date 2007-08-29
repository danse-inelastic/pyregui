#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx



class MainFrame(wx.Frame):
    
    def __init__(self, name, size = (800, 650) ):
        wx.Frame.__init__(self, None, -1, name, wx.DefaultPosition, size)
        self.draw()
        return

    def draw(self):
        self.CreateStatusBar()
        return

    pass # end of MainFrame



# version
__id__ = "$Id$"

# End of file 
