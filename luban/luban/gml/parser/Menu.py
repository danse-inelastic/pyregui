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


class Menu(AbstractNode):


    tag = "menu"
    from luban.gml.elements.Menu import Menu as ElementFactory

    onMenuItem= AbstractNode.onElement

    pass # end of Menu
    


# version
__id__ = "$Id: Menu.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
