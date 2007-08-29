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


class TextField(AbstractNode):


    tag = "textfield"

    from luban.gml.elements.TextField import TextField as ElementFactory 

    pass # end of TextField
    

# version
__id__ = "$Id: TextField.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
