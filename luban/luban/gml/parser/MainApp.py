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


class MainApp(AbstractNode):


    tag = "mainapp"
    from luban.gml.elements.MainApp import MainApp as ElementFactory

    onMainFrame = AbstractNode.onElement

    pass # end of MainApp
    


# version
__id__ = "$Id: MainApp.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
