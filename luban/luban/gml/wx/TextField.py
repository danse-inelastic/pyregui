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


class TextField(wx.TextCtrl):

    def __init__(self, parent, value = '', pos = None, size = (200,-1),
                 name = "" ):
        wx.TextCtrl.__init__(self, parent, id = -1, value = value,
                             pos = pos, size = size, name = name)
        return


    def value(self):
        return self.GetValue()

    pass # end of TextField

# version
__id__ = "$Id$"

# End of file 
