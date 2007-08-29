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
        text = traits.str('text', default='menu')
        tip = traits.str('tip', default='tip?')
        click_callback = traits.str('click-callback', default='None')
        pass
    
    pass # end of Attributes
        


class MenuItem(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onMenuItem(self) 
