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
Using os.system to launch pyre applications for now...

"""


import types


def spawn(command, search_path = 1, dry_run = 0, env = None, 
          remote = False, remote_server = "", rsh = "rsh -.",
          logfile = "run.log", errlogfile = None):
    """
    command: command to run
    env: environment variables to pass to the process in which the command will be executed
    search_path: search for command in PATH
    dry_run: if true, only print the command to be excuted
    remote: if true, spawn on remote host
    remote_server: if remote is true, the server to run the command
    rsh: rsh comand to connect to remote server. default "rsh -."
    logfile: log file name
    errlogfile: error log file name. default to logfile
    """

    if type(command) == list:
        cmd = ' '.join(command)
    else:
        assert(type(command) == types.StringType)
        cmd = command
        pass
    #this implementation is not good enough. it will have problems when
    #'cmd' has quotes in it
    #"echo $?" is used to get exit code from rsh
    #but this trick does not get the job done when mpiexec is used to
    #lauch parallel job. mpiexec does not return a non-zero exit code
    #when subprocess are doing wrong. how to solve this problem??
    if remote: cmd = r'%s %s "%s %s" \; echo $?' % (
        rsh, remote_server, envvar_assignments(env), cmd)
    if dry_run:
        print "Command to execute: \n%s" % cmd
        return 

    print "Executing: \n%s" % cmd
    #if ret: raise "%s failed" % cmd
    import subprocess
    log = open( logfile, 'w' ); log.write( cmd+'\n' ); log.close()
    log = open( logfile, 'a' )
    
    if errlogfile : errlog = open(errlogfile, 'w+' )
    else: errlog = log

    if remote: p = subprocess.Popen( cmd, stdout = log, stderr = errlog, shell = True)
    else: p = subprocess.Popen(
        cmd, stdout = log, stderr = errlog, shell = True, env = env)
    ret = p.wait()
    del p
    log.close(); errlog.close()
    
    log = open( logfile, 'r')
    outputs = log.readlines()
    log.close()
    msg = "Error: %s failed\n" % cmd
    msg += "Outputs: \n%s" % ''.join( outputs[-5:] )
    
    if remote: ret = int(outputs[-1].strip())
    if ret:
        import sys
        print >>sys.stderr, ''.join(outputs)
        raise RuntimeError, msg
    return


def envvar_assignments(env):
    if env is None: env = {}
    r = []
    for key,val in env.iteritems(): r.append( "%s=%s" % (key,val) )
    return ' && '.join(r)




import unittest

from unittest import TestCase

class Spawn_TestCase(TestCase):

    def test_localenv(self):
        "spawn: local, env"
        logfile="test_localenv.log" 
        spawn( "env | grep XXX", remote=0, env={"XXX":"hello"}, logfile = logfile )
        assignment = findAssignment( logfile, "XXX" )
        self.assert_( assignment )
        XXX = todict( assignment ) .get("XXX")
        self.assert_( XXX == "hello" )

        #test env=None
        spawn( "env", remote=0, env=None, logfile = logfile )
        return

    def test_remoteenv(self):
        "spawn: remote, env"
        logfile="test_remoteenv.log"
        spawn( "env | grep XXX", remote=1, remote_server = "n01", env={"XXX":"hello"},
               logfile = logfile )
        assignment = findAssignment( logfile, "XXX" )
        self.assert_( assignment )
        XXX = todict( assignment ) .get("XXX")
        self.assert_( XXX == "hello" )

        #test env=None
        spawn( "env", remote=1, remote_server = "n01", env=None, logfile = logfile )
        return

    def test_local(self):
        "spawn: local"
        spawn( "echo", remote=0)
        return

    def test_remote(self):
        "spawn: remote"
        spawn( "echo", remote=1, remote_server = "n01")
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
