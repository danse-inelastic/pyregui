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


class Panel(AbstractNode):


    tag = "panel"
    from luban.gml.elements.Panel import Panel as ElementFactory

    onSizer = AbstractNode.onElement

    pass # end of Panel
    


# version
__id__ = "$Id: Panel.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
