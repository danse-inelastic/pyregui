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

from Element import Element

from AttributeInventory import AttributeInventory
class Attributes(AttributeInventory):
    
    class Inventory( AttributeInventory.Inventory ):

        import traits
        title = traits.str( "title", default = "title" )
        pass
    
    pass # end of Attributes
        

class RadioBox(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onRadioBox(self) 
