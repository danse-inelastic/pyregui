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


class Table(AbstractNode):


    tag = "table"
    from luban.gml.elements.Table import Table as ElementFactory

    onRow = AbstractNode.onElement

    pass # end of Table

# version
__id__ = "$Id: Table.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
