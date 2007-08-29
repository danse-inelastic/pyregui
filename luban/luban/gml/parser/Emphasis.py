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


from AbstractNode import AbstractNode, debug


class Emphasis(AbstractNode):


    tag = "emphasis"

    from luban.gml.elements.Emphasis import Emphasis as ElementFactory 

    onParagraph = onEmphasis = AbstractNode.onElement    

    pass # end of Emphasis
    

# version
__id__ = "$Id: Emphasis.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
