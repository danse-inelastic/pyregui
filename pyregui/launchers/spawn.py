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
For executing a command and catch output and error output.
error code is returned.
error code is also printed out to the end of the
"""


import types, sys


def spawn(command, dry_run = 0, env = None, 
          logstream = None, errlogstream = None):
    """
    command: command to run
    env: environment variables to pass to the process in which the command will be executed
    dry_run: if true, only print the command to be excuted
    logstream: output stream
    errlogstream: error log file name. default to logstream
    """
    if logstream is None and errlogstream is None: errlogstream = sys.stderr
    if logstream is None: logstream = sys.stdout
    if errlogstream is None: errlogstream = logstream

    if isinstance(command, list):
        cmd = ' '.join(command)
    else:
        assert isinstance(command, basestring)
        cmd = command
        pass

    if dry_run:
        print " * Command to execute: \n    %s" % cmd
        return 

    print "Executing: %s" % cmd
    
    import subprocess
    #log = open( logfile, 'w' ); log.write( cmd+'\n' ); log.close()
    #log = open( logfile, 'a' )
    logstream.write( cmd + '\n' )

    p = subprocess.Popen(
        cmd, stdout = logstream, stderr = errlogstream, shell = True, env = env)
    ret = p.wait()
    del p

    logstream.write( 'return value: %s\n' % ret )
    #log.close(); errlog.close()
    
    return ret




import unittest

from unittest import TestCase

class Spawn_TestCase(TestCase):

    def test_localenv(self):
        "spawn: local, env"
        logfile = 'test_localenv.log' 
        logstream = open( logfile , 'w' )
        spawn( "env | grep XXX", env={"XXX":"hello"}, logstream = logstream )
        logstream.close()
        assignment = findAssignment( logfile, "XXX" )
        self.assert_( assignment )
        XXX = todict( assignment ) .get("XXX")
        self.assert_( XXX == "hello" )

        #test env=None
        spawn( "env", env=None, logstream = open(logfile,'w') )
        return

    def test_local(self):
        "spawn: local"
        spawn( "echo")
        return

    pass # end of TestCase


def findAssignment( filename, name ):
    # fine <name>=<value> in file
    ls = open(filename).readlines()
    for l in ls:
        if l.startswith(name): return l.strip()
        continue
    return


def todict( assignment ):
    # parse <name>=<value>
    try:
        left, right = assignment.split( '=' )
        return {left:right}
    except:
        return { }
    raise "should not reach here"


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
