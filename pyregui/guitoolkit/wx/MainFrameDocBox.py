
import wx.lib.scrolledpanel as scrolled
import wx


def MainFrameDocBox( parent, pyreapp, size = (480, 100) ):
    docstr = getDocStr( pyreapp )
    docBox = scrolled.ScrolledPanel(
        parent, -1, size=size, \
        style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="docBox" )
    docfgs = wx.FlexGridSizer(cols = 1)
    docStr = wx.StaticText( docBox, -1, docstr )
    docfgs.Add(docStr)
    docBox.SetSizer(docfgs)
    docBox.SetAutoLayout(1)
    docBox.SetupScrolling()
    return docBox


def getDocStr(app):
    candidate = app.__class__.__doc__
    if candidate is not None: return candidate
    else: return "Please consider writing a docstring for %s" % app.__class__
    raise

