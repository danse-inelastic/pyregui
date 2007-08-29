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

class MenuBar(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self)
        return


    def append(self, menu):
        self.Append( menu, menu.text )
        return
    

    pass # end of MenuBar

# version
__id__ = "$Id$"

# End of file 
