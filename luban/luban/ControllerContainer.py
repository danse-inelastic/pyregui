#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# this module is not really useful

class ControllerContainer:

    def __init__(self):
        self._store = {}
        return


    def get(self, name):
        return self._store.get(name)


    def set(self, name, controller):
        self._store[name] = controller
        return

    pass # end of ControllerContainer


# version
__id__ = "$Id$"

# End of file 
