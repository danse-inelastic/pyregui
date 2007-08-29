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


class HistogramPlotPanel:

    def __init__(self, parentWindow, size=(4,3), dpi=75):
        self.parentWindow = parentWindow
        self.size = size
        self.dpi = dpi
        return


    def update(self, hist):
        "update plot with hist"
        raise NotImplementedError


    def savePlot(self, filename):
        "save the plot"
        raise NotImplementedError


    def getPictureTypes(self):
        """return file extension for picture types that can be
        saved by this gui control"""
        raise NotImplementedError
    

    pass # end of HistogramPlotPanel



# version
__id__ = "$Id$"

# End of file 
