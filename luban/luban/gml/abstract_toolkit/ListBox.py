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

class ListBox:

    def __init__(self, parent, style=None, callbacks = {}):
        """ style : ['single choice', 'multiple choice' ]
        """
        self.parent = parent
        self.style = style
        self.callbacks = callbacks
        return


    def getSelection(self):
        "get index of current selection. only work for single-selection listbox"
        raise NotImplementedError


    def update(self, l):
        "update control with the give list"
        raise NotImplementedError


    def select(self, index):
        "change selection"
        raise NotImplementedError
    

    pass # end of ListBox


# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2007/03/08 16:13:43 aivazis Exp $"

# End of file 
