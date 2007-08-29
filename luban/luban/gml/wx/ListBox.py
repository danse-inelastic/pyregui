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

styles = {
    "single choice": wx.LB_SINGLE,
    "multiple choice": wx.LB_EXTENDED,
    }


events = {
    'selectionChange': wx.EVT_LISTBOX ,
    'keydown': wx.EVT_KEY_DOWN , 
    }


class ListBox(wx.ListBox, Extension):

    def __init__(self, parent, style=None, callbacks = {}):
        if style is None: style = "single choice"
        style = styles[ style ]
        wx.ListBox.__init__(self, parent, style = style)
        bindCallbacks( self, events, callbacks)
        return


    def getSelection(self):
        return self.GetSelections()[0]


    def update(self, l):
        self.Set( l )
        return


    def select(self, index):
        self.Select( index )
        return

    pass # end of ListBox

# version
__id__ = "$Id$"

# End of file 
