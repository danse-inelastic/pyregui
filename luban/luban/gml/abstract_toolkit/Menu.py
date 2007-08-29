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


class Menu:

    def __init__(self, text):
        self.text = text
        return


    def append(self, menuitem):
        raise NotImplementedError
    

    pass # end of Menu

# version
__id__ = "$Id$"

# End of file 
