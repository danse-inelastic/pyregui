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


class Splitter(wx.SplitterWindow):

    def __init__(self, parentWindow, minimumPanelSize = None):
        wx.SplitterWindow.__init__(self, parentWindow)
        if minimumPanelSize: self.SetMinimumPaneSize( minimumPanelSize )
        return
    
        
    def add(self, window1, window2, direction=None, sliderPosition = None):
        if direction is None: direction = "vertical"
        if sliderPosition is None: sliderPosition = 250
        if direction == "horizontal":
            self.SplitHorizontally( window1, window2, sliderPosition )
            pass
        elif direction == "vertical":
            self.SplitVertically( window1, window2, sliderPosition )
            pass
        else: raise ValueError , "invalid spliting direction: %s" % direction
        
        self.window1 = window1
        self.window2 = window2
        return        
    
    pass # end of Splitter



# version
__id__ = "$Id$"

# End of file 
