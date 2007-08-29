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

class MenuItem:


    def __init__(self, parentWindow, text, tip="tip", callbacks={}):
        self.parentWindow = parentWindow
        self.text = text
        self.tip = tip
        self.callbacks = callbacks
        return
    

    pass # end of MenuItem



# version
__id__ = "$Id$"

# End of file 
