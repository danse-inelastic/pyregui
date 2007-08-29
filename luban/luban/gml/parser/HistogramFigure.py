#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode


class HistogramFigure(AbstractNode):

    tag = "histogramfigure"
    
    from luban.gml.elements.HistogramFigure import HistogramFigure as ElementFactory

    pass # end of HistogramFigure

# version
__id__ = "$Id: HistogramFigure.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
