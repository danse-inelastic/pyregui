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


class MenuItem(AbstractNode):


    tag = "menuitem"
    from luban.gml.elements.MenuItem import MenuItem as ElementFactory

    onMenuItem= AbstractNode.onElement

    pass # end of MenuItem
    


# version
__id__ = "$Id: MenuItem.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
