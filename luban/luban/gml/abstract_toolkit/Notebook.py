#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class Notebook:

    def __init__(self, parentWindow, borderStyle = None):
        self.parentWindow = parentWindow
        self.borderStyle = borderStyle
        return
    
        
    def add(self, title, page):
        raise NotImplementedError
    
    
    pass # end of Notebook



# version
__id__ = "$Id$"

# End of file 
