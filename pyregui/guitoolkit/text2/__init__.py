#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                   (C) Copyright 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""This tool kit is implemented by using unix tool "dialog", which can
be found at

   http://invisible-island.net/dialog/


Actually, pythondialog is used to call dialog from python:

   http://pythondialog.sourceforge.net/
   
"""


from pyregui.guitoolkit.abstract import *


class MainWindowApp:

    def __init__(self, pyre_app_instance, pyre_app_executable, toolkit ):
        self.pyre_app_instance = pyre_app_instance
        self.pyre_app_executable = pyre_app_executable
        self.toolkit = toolkit
        return


    def MainLoop(self):
        mainFrame = MainFrame( self, -1, self.pyre_app_instance.name,
                               self.toolkit,
                               pyreapp = self.pyre_app_instance,
                               pyreapp_executable = self.pyre_app_executable)
        return
    
    pass



from MainFrame import MainFrame



ID_OK = 111111111
ID_CANCEL = 111111112


from pythondialog import dialog 
dlgFactory = dialog.Dialog(dialog="dialog")

dlgFactory.add_persistent_args(["--backtitle", "pyre terminal ui"])


def messageBox( title, msg ):
    width = max( [len(title)+5, len(msg)+5, 30] )
    width = min( 60, width )
    dlgFactory.msgbox(title + '\n' + msg, width = width)
    return


from InventoryDialog import InventoryDialogLoop, InventoryDialog


from InputBoxFactory import InputBoxFactory



# version
__id__ = "$Id:  2006-09-13 07:00:52Z linjiao $"

# End of file 
