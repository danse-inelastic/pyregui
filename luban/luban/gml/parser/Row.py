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


class Row(AbstractNode):


    tag = "row"
    from luban.gml.elements.Row import Row as ElementFactory

    onCell = AbstractNode.onElement

    pass # end of Row

# version
__id__ = "$Id: Row.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
