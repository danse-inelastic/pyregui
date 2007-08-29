#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Patrick Hung, Caltech
#                        (C) 1998-2006  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def launcher():
    return Serial_launcher()

from Launcher import Launcher

class Serial_launcher(Launcher):
    """
The bare basic pyre application launcher.
    """

    class Inventory(Launcher.Inventory):
        import pyre.inventory
        pass

    def __init__(self, name = 'serial_launcher'):
        Launcher.__init__(self, name)
        return

    def get_command(self):
        return []


    def _configure(self):
        Launcher._configure(self)
        return


# version
__id__ = "$Id: serial_launcher.py,v 1.1 2006/08/03 23:42:43 linjiao Exp $"

# End of file
