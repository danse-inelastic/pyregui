

class MainFrame:

    def __init__(self, parent, id, pyreapp_name, toolkit,
                 logoimage = None, pyreapp = None,
                 pyreapp_executable = None):
        self._createLauncher()
        self.parent = parent
        self.pyreapp_name = pyreapp_name
        self.toolkit = toolkit
        self.logoimage = logoimage
        self.pyreapp = pyreapp
        self.pyreapp_executable = pyreapp_executable
        self.show()
        print
        print "* all configurations are done."
        print
        self.run()
        return


    def show(self):
        self.toolkit.InventoryDialogLoop( self, self.pyreapp, self.toolkit )
        return


    def run(self):
        prompt = " Save configuration <s>,  Save configuration and run <r>,  Quit <q> ? "
        while 1:
            choice = raw_input( prompt )
            if choice == 'q': return
            if choice not in ['s','r'] :
                continue
            self._saveConfiguration()
            if choice == 's': return
            launcherApp = self.launcherApp
            self.toolkit.InventoryDialogLoop( self, launcherApp, self.toolkit, verbosity = 1)
            try:
                launcherApp.run( self.pyreapp_executable )
                m = "%s done successfully" % self.pyreapp_executable
            except Exception, err:
                #import traceback
                #msg = traceback.print_exc()
                m = str(err)
                pass
            self.toolkit.messageBox( m, "" )
            return
        
        return


    def _createLauncher(self):
        from pyregui.LauncherApp import LauncherApp
        self.launcherApp = LauncherApp()
        self.launcherApp.run()
        return


    def _saveConfiguration(self):
        from pyregui.inventory.configurationSaver import toPml
        pyreapp = self.pyreapp
        name = pyreapp.name
        filename = "%s.pml" % name
        toPml( pyreapp, filename )
        return
    

    pass 

