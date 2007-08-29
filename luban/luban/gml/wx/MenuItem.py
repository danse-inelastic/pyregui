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
from ext import *



events = {
    'click': wx.EVT_MENU,
    }


class MenuItem:


    def __init__(self, text="menutext", tip="helptext",
                 callbacks={}, submenu = None):
        from globalID import create
        id = create()

        self.id = id
        self.text = text
        self.tip = tip
        self.submenu = submenu
        self.callbacks = callbacks
        return

    pass # end of MenuItem



# version
__id__ = "$Id$"

# End of file 
