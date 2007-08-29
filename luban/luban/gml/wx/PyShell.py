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

import wx, wx.py
from ext import *

Base = wx.py.shell.Shell

events = {
    'keydown': wx.EVT_KEY_DOWN
    }

class PyShell(Extension, Base):

    def __init__(self, parent, locals = {}, callbacks = {}):
        wx.py.shell.Shell.__init__(self, parent, -1, locals=locals)
        bindCallbacks( self, events, callbacks )
        return

    pass # end of PyShell

# version
__id__ = "$Id$"

# End of file 
