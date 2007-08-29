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


class Cell(AbstractNode):


    tag = "cell"
    from luban.gml.elements.Cell import Cell as ElementFactory

    onLink = onParagraph = onEmphasis = onList = AbstractNode.onElement

    pass # end of Cell

# version
__id__ = "$Id: Cell.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
