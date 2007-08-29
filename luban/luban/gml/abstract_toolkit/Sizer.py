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

class Sizer:

    def __init__(self, direction = "horizontal"):
        self.direction = direction
        return
    

    def add(self, element, proportion, border):
        "add a child"
        raise NotImplementedError
    

    pass # end of Sizer


# version
__id__ = "$Id$"

# End of file 
