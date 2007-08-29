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


class MenuBar(AbstractNode):


    tag = "menubar"
    from luban.gml.elements.MenuBar import MenuBar as ElementFactory

    onMenu= AbstractNode.onElement

    pass # end of MenuBar
    


# version
__id__ = "$Id: MenuBar.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
