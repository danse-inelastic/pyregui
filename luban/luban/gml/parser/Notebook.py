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


class Notebook(AbstractNode):


    tag = "notebook"
    
    from luban.gml.elements.Notebook import Notebook as ElementFactory

    onPanel = AbstractNode.onElement

    pass # end of Notebook
    


# version
__id__ = "$Id: Notebook.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
