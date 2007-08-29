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
from AbstractNode import AbstractNode, debug


class Link(AbstractNode):


    tag = "link"

    from luban.gml.elements.Link import Link as ElementFactory 

    onParagraph = onLink = AbstractNode.onElement    

    pass # end of Link
    

# version
__id__ = "$Id: Link.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
