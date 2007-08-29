from pyre.applications.Script import Script
#from launchers.SerialLauncher import launcher as serial_launcher


class LauncherApp(Script):

    "Help pyregui select launcher"

    class Inventory(Script.Inventory):

        import pyre.inventory
        
        launcher = pyre.inventory.facility("launcher", default = "serial_launcher")
        #                                   factory = serial_launcher)
        launcher.meta['known_plugins'] = [
            "serial_launcher",
            "mpich_launcher",
            "mpich2_launcher",
            "lsf_launcher",]
        pass


    def __init__(self):
        Script.__init__(self, "LauncherApp")
        return


    def main(self, *args):
        if len(args) == 1:
            executable = args[0]
            print "LauncherApp: launcher=%s" % self.launcher
            self.launcher.launch( executable )
            pass
        elif len(args) == 0:
            return
        else:
            raise "Don't know how to launch %s" % (args,)
        return


    def _configure(self):
        Script._configure(self)
        self.launcher = self.inventory.launcher
        return



# $Id: LauncherApp.py,v 1.2 2006/08/05 06:49:28 patrickh Exp $
# end of file
