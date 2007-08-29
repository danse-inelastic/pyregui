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
    'click': wx.EVT_BUTTON , 
    }

ids = {
    'OK': wx.ID_OK,
    'Cancel': wx.ID_CANCEL,
    }


class Button(wx.Button, Extension):

    def __init__(self, parent, callbacks = {}, label = 'OK'):
        label = str(label)
        id = ids.get( label )
        if id is None: id = -1
        wx.Button.__init__(self, parent, id, label)
        bindCallbacks( self, events, callbacks)
        return

    pass # end of Button

# version
__id__ = "$Id$"

# End of file 
