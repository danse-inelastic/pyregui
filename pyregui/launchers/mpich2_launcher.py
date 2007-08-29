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
    return MPICH2_launcher()

from Launcher import Launcher

class MPICH2_launcher(Launcher):
    """
launcher using mpich2
    """

    class Inventory(Launcher.Inventory):
        import pyre.inventory

        mpipython = pyre.inventory.str("mpipython", default="`which mpipython.exe`")
        mpipython.meta['tip'] = "Where is the MPI aware python interpreter (part of the pyre mpi package)."

        command = pyre.inventory.str("command", default="mpiexec")
        command.meta['tip'] = "mpi command to run parallel application"

        nodes = pyre.inventory.int("nodes", default=0)
        nodes.meta['tip'] = "number of nodes"

        pass # end of Inventory


    def __init__(self, name = 'mpich2_launcher'):
        Launcher.__init__(self, name)
        return

    def get_command(self):
        si = self.inventory
        return [str(si.command), "-np", str(si.nodes), str(si.mpipython)]
    #return "%(command)s -np %(nodes)s %(mpipython)s" % kdict
                                                   


# version
__id__ = "$Id: mpich2_launcher.py,v 1.1 2006/08/03 23:42:43 linjiao Exp $"

# End of file
