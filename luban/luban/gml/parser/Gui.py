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


class Gui(AbstractNode):


    tag = "gui"
    from luban.gml.elements.Gui import Gui as ElementFactory

    onDialog = onMainApp = AbstractNode.onElement

    pass # end of Gui
    


# version
__id__ = "$Id: Gui.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
