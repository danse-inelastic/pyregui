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


class ListBox(AbstractNode):


    tag = "listbox"
    from luban.gml.elements.ListBox import ListBox as ElementFactory

    #on???= AbstractNode.onElement

    pass # end of ListBox
    


# version
__id__ = "$Id: ListBox.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
