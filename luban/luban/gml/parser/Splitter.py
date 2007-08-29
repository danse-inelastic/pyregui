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


class Splitter(AbstractNode):


    tag = "splitter"
    from luban.gml.elements.Splitter import Splitter as ElementFactory

    onNotebook = onSplitter = onPanel = AbstractNode.onElement

    pass # end of Splitter
    


# version
__id__ = "$Id: Splitter.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
