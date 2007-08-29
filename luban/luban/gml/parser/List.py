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


class List(AbstractNode):


    tag = "list"
    from luban.gml.elements.List import List as ElementFactory

    onListItem = AbstractNode.onElement

    pass # end of List

# version
__id__ = "$Id: List.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
