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
        self.inithistory()
        bindCallbacks( self, events, callbacks )
        return


    def inithistory(self):
        wxpyshellhistory = self._wxpyshellhistory()
        
        self.newhistory_start_index = 0
        if os.path.isfile(wxpyshellhistory):
            hisfile = file( wxpyshellhistory,'r')
            for l in hisfile.readlines():
                self.history.append(l[:-1])
            hisfile.close()
            self.newhistory_start_index = len(self.history)

        self.history.reverse()
        #print self.history
        #print self.newhistory_start_index
        
        return

    
    def savehistory(self):
        #print 'savehistory'
        wxpyshellhistory = self._wxpyshellhistory()
        history = self.history
        #print history
        if self.newhistory_start_index == 0:
            new = history
        else:
            new = history[ : -self.newhistory_start_index]
            
        new.reverse()
        
        if os.path.exists(wxpyshellhistory): mode = 'a'
        else: mode = 'w'
        f = open( wxpyshellhistory, mode )
        #print wxpyshellhistory, mode
        #print new
        for line in new:
            #print line
            #print f
            f.write( '%s\n' % line )
            continue
        f.close()
        return


    def __del__(self):
        self.savehistory()
        return


    def _wxpyshellhistory(self):
        return os.environ.get('WXPYSHELLHISTORY') or \
               os.path.join( os.path.expanduser( '~' ), '.wxpyshellhistory' )
    
    pass # end of PyShell

import os

# version
__id__ = "$Id$"

# End of file 
