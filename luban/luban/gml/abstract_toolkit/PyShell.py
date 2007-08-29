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

class PyShell:

    def __init__(self, parentWindow, locals = {}, callbacks = {}):
        self.parentWindow = parentWindow
        self.locals = locals
        self.callbacks = callbacks
        return

    pass # end of PyShell

# version
__id__ = "$Id$"

# End of file 
