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


borderStyles = {
    "sunken": wx.BORDER_SUNKEN,
    'default': wx.BORDER_DEFAULT,
    }



class Panel(wx.Panel):
    
    def __init__(self, parentWindow, borderStyle=None):
        style = borderStyles[ borderStyle ]
        wx.Panel.__init__(self, parentWindow, style = style)
        return
    
    pass # end of Panel



# version
__id__ = "$Id$"

# End of file 
