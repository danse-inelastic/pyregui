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


from Panel import borderStyles


class Notebook(wx.Notebook):

    def __init__(self, parentWindow, borderStyle = None):
        style = borderStyles[ borderStyle ]
        wx.Notebook.__init__(self, parentWindow, style = style)
        self.pages = []
        return
    
        
    def add(self, title, page):
        self.AddPage( page, title )
        self.pages.append( page )
        return
    
    pass # end of Notebook



# version
__id__ = "$Id$"

# End of file 
