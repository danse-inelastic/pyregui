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
        direction = traits.str( "direction", default = "vertical" )
        sliderPosition = traits.int( "sliderPosition", default = 100 )
        minimumPanelSize = traits.int( "minimumPanelSize", default = 250 )
        pass
    
    pass # end of Attributes
        

class Splitter(Element):

    AttributeContainer = Attributes
    
    def identify(self, visitor): return visitor.onSplitter(self)

    pass # end of Splitter
