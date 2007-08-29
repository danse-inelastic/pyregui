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


import urllib
from AbstractNode import AbstractNode


class Paragraph(AbstractNode):


    tag = "paragraph"
    from luban.gml.elements.Paragraph import Paragraph as ElementFactory

    onFigure = onTable = onLink = onEmphasis = onList = onCode = AbstractNode.onElement

    pass # end of Paragraph

# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
