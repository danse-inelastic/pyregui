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


class Code(AbstractNode):


    tag = "code"
    from luban.gml.elements.Code import Code as ElementFactory

    pass # end of Code


# version
__id__ = "$Id: Code.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
