#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import journal
debug = journal.debug("HistogramPlotPanel")
warning = journal.warning("HistogramPlotPanel")


import wx

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg, Toolbar, FigureManager
from matplotlib.figure import Figure


class HistogramPlotPanel(wx.Panel):

    def __init__(self, parentWindow, size=(4,3), dpi=75):
        wx.Panel.__init__(self, parentWindow, id=-1)

        import wxmpl.wxmpl as wxmpl
        self.canvas = wxmpl.PlotPanel(self, -1, size = size, dpi = dpi)
        self.figure = self.canvas.figure
        self.figure.add_subplot(111)
        
##         self.toolbar = Toolbar(self.canvas)
##         self.toolbar.Realize()

        # On Windows, default frame size behaviour is incorrect
        # you don't need this under Linux
##         tw, th = self.toolbar.GetSizeTuple()
##         fw, fh = self.canvas.GetSizeTuple()
##         self.toolbar.SetSize(wx.Size(fw, th))

        # Create a figure manager to manage things
        self.figmgr = FigureManager(self.canvas, 1, self)
        # Now put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT|wx.TOP|wx.GROW)

        # add a spacer between figure and toolbar
        #sizer.AddSpacer( (10,10) )
        
        # Best to allow the toolbar to resize!
        #sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
        self.sizer = sizer
        self.SetAutoLayout(1)
        sizer.Fit(self)
        
        #FigureCanvasWxAgg.__init__(self, parentWindow, id, Figure(size, dpi) )
        from histogram.plotter import HistogramMplPlotter as HMP
        self.plotter = HMP( self.figure )
        self.plot = Plot(self)
        self.image = None
        return


    def update(self, hist):
        self.plotter.clear()
        self.Refresh()
        try:
            self.plotter.plot( hist )
            self.image = self.plotter.image()
        except Exception, err:
            print "%s: %s" % (err.__class__.__name__, err)
            self.plot.clear()
            pass
        self.Refresh()
        return


    def savePlot(self, filename):
        "use the plot"
        self.canvas.print_figure(filename)
        return


    def getPictureTypes(self):
        """return file extension for picture types that can be
        saved by this gui control"""
        canvas = self.canvas
        # Fetch the required filename and file type.

        # wx 2.6: getPictureTypes return a string
        # wx 2.8: getPictureTypes return a tuple
        tmp = canvas._get_imagesave_wildcards()
        
        if '__iter__' in dir(tmp):
            # wx 2.8
            filetypesstr, filetypeslist, n = tmp
        else:
            # wx 2.6
            filetypesstr = tmp
            
        return filetypesstr


    def makePylabUsable(self):
        "make pylab commands plot to my canvas"
        def gcf(): return self.figure
        def gci(): return self.plotter.image()
        
        import matplotlib.pylab as mp
        import pylab

        tobeoveride = [ mp, pylab ]

        #for newer matplotlib (for example 0.91.2), plotting functions
        #are in matplotlib.pyplot
        try:
            import matplotlib.pyplot as mp
            tobeoveride.append( mp )
        except ImportError:
            pass

        for m in tobeoveride:
            m.gcf = gcf
            m.gci = gci
            continue
        return 
    

    def GetToolBar(self):
        return
        return self.toolbar


    pass # end of HistogramPlotPanel



class Plot(object):
    """ a proxy to the plot contained in HistogramPlotPanel """

    def __init__(self, plotPanel):
        self.plotPanel = plotPanel
        self.figure = plotPanel.figure
        return


    # obsolete
##     def replot(self, *args, **kwds):
##         self.plotPanel.plotter.plot( *args, **kwds )
##         return


    def __getattribute__(self, name):
        if name in [ 
            'figure', 'plotPanel', #'replot',
            ]: return object.__getattribute__(self, name)
        try:
            return getattr(self.plotPanel, name)
        except:
            try:
                return getattr(self.figure, name )
            except:
                return getattr(self.figure.gca(), name)
            raise
        raise

    pass

    

def test():
    class MainFrame(wx.Frame):
        
        def __init__(self, parentWindow=None, id=-1, name = "hello", pos = wx.DefaultPosition):
            wx.Frame.__init__(self, parentWindow,id,name, pos, (640,480))
            self.panel = HistogramPlotPanel(self)
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self.panel, 1, wx.ALL|wx.EXPAND, 5)
            self.SetSizer(sizer)
            self.Fit()
            return

        pass # end of MainFrame

    WxPyAppBase = wx.PySimpleApp
    
    class MainWinApp(WxPyAppBase):
        
        def __init__(self,   *args, **kwargs):
            import os
            WxPyAppBase.__init__(self, *args, **kwargs)
            return
        

        def OnInit(self):
            self.frame = MainFrame(None, -1)
            self.SetTopWindow(self.frame)
            self.frame.Show(True)
            return True

        pass

    mainWin = MainWinApp()
    plotPanel = mainWin.frame.panel
    figure = plotPanel.figure
    axes = figure.gca()
    axes.plot([1,2,3],[1,2,3])
    #plotPanel.draw()
    mainWin.MainLoop()

    return


if __name__  == "__main__": test()
    

# version
__id__ = "$Id$"

# End of file 
