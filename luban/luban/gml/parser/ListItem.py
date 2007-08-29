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


class ListItem(AbstractNode):


    tag = "listitem"
    from luban.gml.elements.ListItem import ListItem as ElementFactory

    onLink = onParagraph = AbstractNode.onElement

    pass # end of ListItem

# version
__id__ = "$Id: ListItem.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
