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


class Section(AbstractNode):


    tag = "section"
    
    from luban.gml.elements.Section import Section as ElementFactory

    onFigure = onList = onEmphasis = onSection = onNote = onParagraph = onTable = onCode = onLink = AbstractNode.onElement

    pass #end of Section
    

# version
__id__ = "$Id: Section.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
