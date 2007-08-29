

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
        logfile.meta['tip'] = "file to save output"

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
        spawn(cmds, search_path = si.search_path, dry_run = si.dry_run,
              env = eval(si.env),
              remote = si.remote, remote_server = si.remote_server, rsh = si.rsh,
              logfile = si.logfile)
        return


    def get_command(self): self._nie( "get_command" )


    def _nie(self, method):
        raise NotImplementedError , "class %s must implement method %s" % (
            self.__class__.__name__, method)


    pass # end of class Launcher 
