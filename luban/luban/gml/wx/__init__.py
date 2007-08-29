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
    """app( name ) --> new app
    """
    from MainWinApp import MainWinApp
    return MainWinApp(name)


def mainFrame( name, **kwds ):
    "mainFrame(name) --> new main frame"
    from MainFrame import MainFrame
    return MainFrame( name, **kwds )


## def view( *args, **kwds ):
##     "view( app ) --> new view of a wx application"
##     from View import View
##     return View( *args, **kwds )


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
    import wx
    text = wx.StaticText( parentWindow, -1, txt )
    return text


def sizer( **kwds ):
    from Sizer import Sizer
    return Sizer( **kwds )


def listbox(parentWindow, **kwds):
    from ListBox import ListBox
    return ListBox( parentWindow, **kwds )


def menu(parentWindow, text):
    from  Menu import Menu
    return Menu(parentWindow, text)


def menubar():
    from MenuBar import MenuBar
    return MenuBar()


def menuitem(text, **kwds):
    from MenuItem import MenuItem
    return MenuItem( text, **kwds)


def loadfileDialog(parentWindow, title, defaultDir = '.'):
    import wx
    d = wx.FileDialog( parentWindow, title, defaultDir = defaultDir)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    file = d.GetPath()
    d.Destroy()
    return file


def textentryDialog( parentWindow, caption, message, default = "Input your text" ):
    import wx
    d = wx.TextEntryDialog(
        parentWindow, message=message, caption=caption, defaultValue = default)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    value = d.GetValue()
    d.Destroy()
    return value


def dirDialog( parentWindow, title, defaultDir = "." ):
    import wx
    d = wx.DirDialog( parentWindow, title, defaultDir)
    if d.ShowModal() != wx.ID_OK: d.Destroy(); return
    path = d.GetPath()
    d.Destroy()
    return path


def messageDialog(parentWindow, title, message):
    import wx
    d= wx.MessageDialog( parentWindow, message, title, wx.OK)
    d.ShowModal() # Shows it
    d.Destroy() # finally destroy it when finished.
    return


def savefileDialog(parentWindow, title, filetypes):
    import wx
    dlg =wx.FileDialog(parentWindow, title, "", "", filetypes,
                       wx.SAVE|wx.OVERWRITE_PROMPT|wx.CHANGE_DIR)
    rt = None
    if dlg.ShowModal() == wx.ID_OK:
        dirname  = dlg.GetDirectory()
        filename = dlg.GetFilename()
        import os
        rt = os.path.join(dirname, filename)
        pass
    dlg.Destroy()
    return rt


def dialog(parentWindow, **kwds ):
    from Dialog import Dialog
    return Dialog( parentWindow, **kwds )


def button(parentWindow, **kwds ):
    from Button import Button
    return Button( parentWindow, **kwds )


def textfield(parentWindow, **kwds ):
    from TextField import TextField
    return TextField( parentWindow, **kwds )


def histogramFigure( parentWindow, **kwds):
    from HistogramPlotPanel import HistogramPlotPanel
    return HistogramPlotPanel( parentWindow, **kwds )


def pyshell(parentWindow, **kwds):
    from PyShell import PyShell
    return PyShell( parentWindow, **kwds )

# version
__id__ = "$Id$"

# End of file 
