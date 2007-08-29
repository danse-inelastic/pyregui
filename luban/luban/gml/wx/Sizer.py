#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import wx


directions = {
    "horizontal": wx.HORIZONTAL,
    "vertical": wx.VERTICAL,
    }
    


class Sizer(wx.BoxSizer):

    def __init__(self, direction = "horizontal"):
        direction = directions[direction]
        wx.BoxSizer.__init__(self, direction)
        return
    

    def add(self, element, proportion, border):
        return wx.Sizer.Add(self, element, proportion, wx.GROW | wx.ALL, border)
        return wx.Sizer.Add(self, element, proportion, wx.EXPAND, border)
    

    pass # end of Sizer

# version
__id__ = "$Id$"

# End of file 
