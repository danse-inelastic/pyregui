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
    return LSF_launcher()


from Launcher import Launcher
import sys, os

def available_queues():
    from subprocess import Popen, PIPE, STDOUT
    try:
        p = Popen("bqueues", shell=True, stdout=PIPE, stderr=STDOUT, close_fds=True)
        out = [line.split()[0] for line in p.stdout.readlines()[1:] ]
        return out
    except:
        print "no bqueues"
        return []


class LSF_launcher(Launcher):
    """
Use this launcher on the CITerra cluster, which has myrinet and uses lsf.
    """

    class Inventory(Launcher.Inventory):
        import pyre.inventory

        mpipython = pyre.inventory.str("mpipython", default="`which mpipython.exe`")
        mpipython.meta['tip'] = "Where is the MPI aware python interpreter (part of the pyre mpi package)."

        command = pyre.inventory.str("command", default="bsub")

        nodes = pyre.inventory.int("nodes", default=0)

        timelimit = pyre.inventory.str("timelimit", default="00:02")
        timelimit.meta['tip'] = "Sets the time limit of the job. format is Hour:Minutes."

        queue = pyre.inventory.str("queue", default="normal")
        queue.meta['known_alternatives'] = available_queues()
        queue.meta['tip'] = "What queue to run on."

        basename = os.path.basename(sys.argv[0])
        if len(sys.argv) >= 2 and basename.startswith('wxapp'):
            defaultname = sys.argv[1]
        else:
            defaultname = 'PyreApp'

        jobname = pyre.inventory.str("jobname", default=defaultname)
        jobname.meta['tip'] = "The name of the job. Just an identifier."

    def __init__(self, name = "lsf_launcher"):
        Launcher.__init__(self, name)
        return

    def get_command(self):
        si = self.inventory
        return [si.command,
                "-W%s" % si.timelimit,
                "-n %s" % si.nodes,
                "-o ./%%J.out",
                "-a mpich_gm",
                "-q %s" % si.queue,
                "-J %s" % si.jobname,
                "gmmpirun_wrapper",
                "%s" % si.mpipython,
                ]
    #return "%(command)s -W%(timelimit)s -n %(nodes)s -o ./%%J.out -a mpich_gm -q %(queue)s -J %(jobname)s gmmpirun_wrapper %(mpipython)s" % kdict

if __name__ == '__main__':
    print available_queues()
    
# version
__id__ = "$Id: lsf_launcher.py,v 1.3 2006/08/10 01:38:35 patrickh Exp $"

# End of file
