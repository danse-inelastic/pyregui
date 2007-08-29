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


class PyShell(AbstractNode):


    tag = "pyshell"
    
    from luban.gml.elements.PyShell import PyShell as ElementFactory

    #on???= AbstractNode.onElement

    pass # end of PyShell
    


# version
__id__ = "$Id: PyShell.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
