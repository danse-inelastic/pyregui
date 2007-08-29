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
        self.app = None # needs app to hold wxapp instance so that we know how
        #to initialize
        return


    def start(self):
        """ start the main view """
        # this should be called after self.app is assigned with
        # an instance of MainWinApp
        self.app.start()
        return


    def end(self):
        """ end the main view """
        self.app.end()
        return
        
    
    pass # end of MainView


# version
__id__ = "$Id$"

# End of file 

