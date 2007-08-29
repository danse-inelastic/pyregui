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


class Splitter:

    def __init__(self, parentWindow, minimumPanelSize = None):
        self.parentWindow = parentWindow
        self.minimumPanelSize = minimumPanelSize
        return
    
        
    def add(self, window1, window2, direction=None, sliderPosition = None):
        raise NotImplementedError
    
    
    pass # end of Splitter



# version
__id__ = "$Id$"

# End of file 
