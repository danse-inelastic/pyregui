#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                          (C) 2007  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from AttributeInventory import AttributeInventory


class Attributes(AttributeInventory):
    
    class Inventory( AttributeInventory.Inventory ):

        import traits
        borderStyle = traits.str('borderStyle', default="default" )
        label = traits.str('label', default = "label")
        pass
    
    pass # end of Attributes
        

from Element import Element

class Panel(Element):

    AttributeContainer = Attributes
    
    def identify(self, visitor): return visitor.onPanel(self) 
