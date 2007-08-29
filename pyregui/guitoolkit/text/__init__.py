

class MainWindowApp:

    def __init__(self, pyre_app_instance, pyre_app_executable, toolkit ):
        self.pyre_app_instance = pyre_app_instance
        self.pyre_app_executable = pyre_app_executable
        self.toolkit = toolkit
        return


    def MainLoop(self):
        mainFrame = self.toolkit.MainFrame(
            self, -1, self.pyre_app_instance.name,
            self.toolkit,
            pyreapp = self.pyre_app_instance,
            pyreapp_executable = self.pyre_app_executable)
        return
    
    pass



from MainFrame import MainFrame



ID_OK = 111111111
ID_CANCEL = 111111112


def messageBox( title, msg ):
    border = '-' * min( max(len(title)+4, len(msg) + 2 ), 77)
    print border
    print '*', title, '*'
    print '  ', msg
    print border
    return


class GridSizer:

    def __init__(self, ncols, nrows):
        self.ncols = ncols
        self.nrows = nrows
        return


    def Add( self, obj, pos = (0,0) ):
        #pos = (row,col)
        row, col = pos
        obj.show()
        return

    pass



from InventoryDialog import InventoryDialogLoop, InventoryDialog


from InputBoxFactory import InputBoxFactory

from SetButtonFactory import SetButtonFactory

from TraitLabelFactory import TraitLabelFactory
