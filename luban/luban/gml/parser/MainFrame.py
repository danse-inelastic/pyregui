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


class MainFrame(AbstractNode):


    tag = "mainframe"
    from luban.gml.elements.MainFrame import MainFrame as ElementFactory

    onMenuBar = onPanel = onSplitter = AbstractNode.onElement

    pass # end of MainFrame
    


# version
__id__ = "$Id: MainFrame.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
