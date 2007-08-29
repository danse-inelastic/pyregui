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


class Sizer(AbstractNode):


    tag = "sizer"
    from luban.gml.elements.Sizer import Sizer as ElementFactory

    onPanel = onTextField = onButton = onPyShell = onHistogramFigure = onSizer = onListBox = AbstractNode.onElement

    pass # end of Sizer
    


# version
__id__ = "$Id: Sizer.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
