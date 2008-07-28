#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                                  Patrick Hung
#                        (C) 2006-2008  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component

class Launcher(Component):
    """
base class for pyre application launcher.
    """

    class Inventory(Component.Inventory):
        import pyre.inventory as inv
        dry_run = inv.bool( "dry_run", default = 0)
        dry_run.meta['tip'] = "  If 'dry_run' is true, the command will not actually be run"

        search_path = inv.bool( "search_path", default = 1)
        search_path.meta['tip'] = \
            " (from distutils.spawn.spawn): "\
            "If 'search_path' is true (the default), the system's executable "\
            "search path will be used to find the program; otherwise, cmd[0] "\
            "must be the exact path to the executable"

        logfile = inv.str( 'logfile', default = "run.log")
        logfile.meta['tip'] = "file to save output. if empty, stdout will be used"

        errlogfile = inv.str( "errlogfile", default = "")
        errlogfile.meta['tip'] = "file to save error output. if empty, logfile will be used. If logfile is also empty, stderr will be used"

        remote = inv.bool("remote", default=0)
        remote.meta['tip'] = "if 'remote' is true, parallel application will be started from a remote server"

        remote_server = inv.str("remote_server", default = "")
        remote_server.meta['tip'] = "if 'remote' is true, 'remote_server' will be used to start the parallel aplication"

        rsh = inv.str("rsh", default = "rsh -. ")
        rsh.meta['tip'] = "rsh(ssh) command to connect to server that is going to start the parallel application"

        env = inv.str("env", default = "None" )
        env.meta['tip'] = """environment variables pass to the program to be launched. eg. {"CC":"gcc"}"""

        pass # end of Inventory


    def __init__(self, name, facility = "launcher"):
        Component.__init__(self,name,facility)
        return


    def launch(self, executable):
        print "%s.launch(%s)" % (self.__class__.__name__, executable)
        cmds = self.get_command()
        cmds.append ( executable )
        print "%s.commands=%s" % (self.__class__.__name__, cmds)

        from spawn import spawn
        si = self.inventory

        logstream = self.logstream
        errlogstream = self.errlogstream
        
        if si.remote:
            from remote_spawn import remote_spawn as spawn
            ret = spawn(
                cmds, dry_run = si.dry_run, env = eval(si.env),
                logstream = logstream, errlogstream = errlogstream,
                remote_server = si.remote_server, rsh = si.rsh,
                )
        else:
            from spawn import spawn
            ret = spawn(
                cmds, dry_run = si.dry_run, env = eval(si.env),
                logstream = logstream, errlogstream = errlogstream,
                )

        if ret:
            msg = "Error: %s failed\n" % executable
            import sys
            print >>sys.stderr, msg
            raise RuntimeError, msg

        return


    def get_command(self): self._nie( "get_command" )


    def _configure(self):
        Component._configure(self)
        self.logfile = self.inventory.logfile
        errlogfile = self.inventory.errlogfile
        if errlogfile == '': errlogfile = self.logfile
        self.errlogfile = errlogfile
        return


    def _init(self):
        Component._init(self)

        import sys
        if len(self.logfile) == 0:
            logstream = sys.stdout
        else:
            logstream = open( self.logfile, 'w' )
        self.logstream = logstream

        if self.errlogfile == self.logfile:
            if len (self.errlogfile) == 0:
                errlogstream = sys.stderr
            else:
                errlogstream = self.logstream
        else:
            errlogstream = open(self.errlogfile, 'w')
        self.errlogstream = errlogstream
        
        return


    def _fini(self):
        Component._fini(self)
        import sys
        if self.logstream != sys.stdout: self.logstream.close()
        if self.errlogstream != sys.stderr and self.errlogstream != self.logstream:
            self.errlogstream.close()
        return


    def _nie(self, method):
        raise NotImplementedError , "class %s must implement method %s" % (
            self.__class__.__name__, method)


    pass # end of class Launcher 




import unittest

from unittest import TestCase

class Launcher_TestCase(TestCase):

    class TrivialLauncher( Launcher ):
        def get_command(self): return []

    def test1(self):
        "launcher"
        launcher = self.TrivialLauncher('testlauncher')
        launcher.inventory.logfile = ""
        launcher.inventory.errlogfile = ""
        launcher._configure()
        launcher._init()
        launcher.launch( 'echo hello' )
        launcher._fini()
        return

    def test2(self):
        "launcher"
        launcher = self.TrivialLauncher('testlauncher')
        launcher.inventory.logfile = logfile =  "run.log"
        launcher.inventory.errlogfile = errlogfile = "error.log"
        launcher._configure()
        launcher._init()
        launcher.launch( 'python -c "print 1; import sys; print >> sys.stderr, 2"' )
        launcher._fini()

        # verify outputs
        lines = open(logfile).readlines()
        found = False
        for line in lines:
            try: v = eval(line)
            except: continue
            if v == 1: found = True; break
            continue
        if not found: raise "Should found outputs in %s" % logfile

        lines = open(errlogfile).readlines()
        self.assertEqual( len(lines), 1 )
        self.assertEqual( eval( lines[0] ), 2 )
        return

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(Launcher_TestCase)
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
    

# $Id$
# end of file
