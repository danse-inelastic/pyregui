#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def mainView():
    from MainView import MainView
    return MainView()


def app(name):
    "app( name ) --> new app"
    from MainWinApp import MainWinApp
    return MainWinApp(name)


def mainFrame( name, **kwds ):
    "mainFrame(name) --> new main frame"
    from MainFrame import MainFrame
    return MainFrame( name, **kwds )


def panel( parentWindow, **kwds ):
    from Panel import Panel
    return Panel( parentWindow, **kwds )


def splitter( parentWindow, **kwds):
    from Splitter import Splitter
    return Splitter( parentWindow, **kwds)


def notebook( parentWindow, **kwds):
    from Notebook import Notebook
    return Notebook( parentWindow, **kwds)


def text( parentWindow, txt):
    raise NotImplementedError


def sizer( **kwds ):
    from Sizer import Sizer
    return Sizer( **kwds )


def listbox(parentWindow, **kwds):
    from ListBox import ListBox
    return ListBox( parentWindow, **kwds )


def menu(text):
    from  Menu import Menu
    return Menu(text)


def menubar():
    from MenuBar import MenuBar
    return MenuBar()


def menuitem(parentWindow, text, **kwds):
    from MenuItem import MenuItem
    return MenuItem( parentWindow, **kwds )


def loadfileDialog(parentWindow, title):
    """show a dialog to choose a file. return the path to the file.
    """
    raise NotImplementedError


def savefileDialog(parentWindow, title, filetypes):
    """show a dialog to choose a path to which a new path will
    be created. prompt if override.

    return the path
    """
    raise NotImplementedError


#non-standard controls
def histogramFigure( parentWindow, **kwds):
    raise NotImplementedError


def pyshell(parentWindow, **kwds):
    raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
