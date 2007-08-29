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


class Figure(AbstractNode):

    tag = "figure"
    
    from luban.gml.elements.Figure import Figure as ElementFactory

    pass # end of Figure

# version
__id__ = "$Id: Figure.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
