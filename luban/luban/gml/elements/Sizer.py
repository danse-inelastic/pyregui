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
        ratios = traits.list( "ratios", default = [] )
        border = traits.int( "border", default = 5 )
        direction = traits.str( "direction", default = "horizontal", validator=\
                                traits.choice( ["horizontal", "vertical"] ) )
        pass
    
    pass # end of Attributes
        

class Sizer(Element):

    AttributeContainer = Attributes
    
    def identify(self, visitor): return visitor.onSizer(self)

    pass # end of Sizer
