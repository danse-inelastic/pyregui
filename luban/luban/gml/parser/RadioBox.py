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


class RadioBox(AbstractNode):


    tag = "radiobox"
    from luban.gml.elements.RadioBox import RadioBox as ElementFactory

    #on???= AbstractNode.onElement

    pass # end of RadioBox
    


# version
__id__ = "$Id: RadioBox.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
