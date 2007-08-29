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


from luban.View import View as ViewBase


class MainView(ViewBase):

    def __init__(self):
        ViewBase.__init__(self)
        return


    def start(self):
        """ start the main view """
        raise NotImplementedError
    
    
    pass # end of MainView


# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2007/03/08 16:13:43 aivazis Exp $"

# End of file 

