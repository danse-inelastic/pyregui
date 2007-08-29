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
    return MPICH_launcher()

from Launcher import Launcher

class MPICH_launcher(Launcher):
    """
The bare basic pyre application launcher.
    """

    class Inventory(Launcher.Inventory):
        import pyre.inventory

        mpipython = pyre.inventory.str("mpipython", default="`which mpipython.exe`")
        mpipython.meta['tip'] = "Where is the MPI aware python interpreter (part of the pyre mpi package)."

        command = pyre.inventory.str("command", default="mpirun")

        nodes = pyre.inventory.int("nodes", default=0)

    def __init__(self, name = 'mpich_launcher'):
        Launcher.__init__(self, name)
        return

    def get_command(self):
        si = self.inventory
        return [str(si.command), "-np", str(si.nodes), str(si.mpipython)]
    #return "%(command)s -np %(nodes)s %(mpipython)s" % kdict
                                                   


# version
__id__ = "$Id: mpich_launcher.py,v 1.1 2006/08/03 23:42:43 linjiao Exp $"

# End of file
