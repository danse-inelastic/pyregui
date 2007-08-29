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


from AbstractNode import AbstractNode, debug


class Button(AbstractNode):


    tag = "button"

    from luban.gml.elements.Button import Button as ElementFactory 

    pass # end of Button
    

# version
__id__ = "$Id: Button.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
