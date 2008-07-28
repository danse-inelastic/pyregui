#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Pyre Development Team
#                        (C) 1998-2006  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
to execute a command on a remote machine, and catch the output and error output
"""


import types, sys


def remote_spawn(
    command, dry_run = 0, env = None,
    logstream = None, errlogstream = None, 
    remote_server = "", rsh = "rsh -.",
    ):
    """
    command: command to run
    env: environment variables to pass to the process in which the command will be executed
    dry_run: if true, only print the command to be excuted
    logstream: output stream
    errlogstream: error log file name. default to logstream
    remote_server: if remote is true, the server to run the command
    rsh: rsh comand to connect to remote server. default "rsh -."
    """

    #this implementation is not tested well enough. it probably will fail
    #if the cmd is strange.
    cmd = r'''%s %s %s %s''' % (
        rsh, remote_server, envvar_assignments(env), command)

    from spawn import spawn
    return spawn(
        cmd, dry_run = dry_run, logstream = logstream, errlogstream = errlogstream)



def envvar_assignments(env):
    if env is None: env = {}
    r = []
    for key,val in env.iteritems(): r.append( "%s=%s" % (key,val) )
    return ' && '.join(r)




import unittest

from unittest import TestCase

class Spawn_TestCase(TestCase):

    def test_remoteenv(self):
        "spawn: remote, env"
        logfile="test_remoteenv.log"
        logstream = open( logfile, 'w' )
        remote_spawn( "env | grep XXX", remote_server = "localhost", env={"XXX":"hello"},
               logstream = logstream, rsh = 'ssh' )
        logstream.close()
        assignment = findAssignment( logfile, "XXX" )
        self.assert_( assignment )
        XXX = todict( assignment ) .get("XXX")
        self.assert_( XXX == "hello" )

        #test env=None
        remote_spawn( "env", remote_server = "localhost", env=None, rsh = 'ssh' )
        return

    def test_remote(self):
        "spawn: remote"
        remote_spawn( "echo", remote_server = "localhost", rsh = 'ssh')
        return

    pass # end of TestCase

from spawn import findAssignment, todict


def pysuite():
    suite1 = unittest.makeSuite(Spawn_TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    import journal
##     journal.debug('instrument').activate()
##     journal.debug('instrument.elements').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# $Id: spawn.py,v 1.3 2006/08/10 02:06:49 patrickh Exp $
# end of file
