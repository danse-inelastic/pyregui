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


class Dialog(AbstractNode):


    tag = "dialog"

    from luban.gml.elements.Dialog import Dialog as ElementFactory 

    onPanel = onButton = onSizer = AbstractNode.onElement

    pass # end of Dialog
    

# version
__id__ = "$Id: Dialog.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
