

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
        self.toolkit.messageBox( "* all configurations are done.", '' )
        self.run()
        return


    def show(self):
        self.toolkit.InventoryDialogLoop( self, self.pyreapp, self.toolkit )
        return


    def run(self):
        df = self.toolkit.dlgFactory
        dlloop = self.toolkit.InventoryDialogLoop
        prompt = self.pyreapp.name
        choices  = [
            ('s', "Save settings"),
            ('r', "Save settings, and run application"),
            ('q', "Quit"),
            ]
        while 1:
            code, choice = df.menu(
                prompt,
                width = 60,
                choices = choices)
            if code in (df.DIALOG_CANCEL, df.DIALOG_ESC): continue
            if choice == 'q': return
            if choice not in ['s','r'] :
                continue
            self._saveConfiguration()
            if choice == 's': return
            launcherApp = self.launcherApp
            dlloop( self, launcherApp, self.toolkit, verbosity = 1)
            self._saveLauncherConfiguration()
            try:
                launcherApp.run( self.pyreapp_executable )
                m = "%s done successfully" % self.pyreapp_executable
            except Exception, err:
                #import traceback
                #msg = traceback.print_exc()
                m = "%s: %s" % (err.__class__.__name__, err)
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
        saveConfiguration( self.pyreapp )
        return
    

    def _saveLauncherConfiguration(self):
        saveConfiguration( self.launcherApp )
        return


    pass 


def saveConfiguration( pyreapp ):
    from pyregui.inventory.configurationSaver import toPml
    name = pyreapp.name
    filename = "%s.pml" % name
    toPml( pyreapp, filename )
    return
