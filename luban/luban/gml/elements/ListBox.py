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
        style = traits.str(
            "style", default = "single choice",
            validator = traits.choice( ['single choice', 'multiple choice'] )
            )
        label = traits.str( 'label', default= "listbox" )
        selectionChange_callback = traits.str('selectionChange-callback', default = '')
        keydown_callback = traits.str('keydown-callback', default = '')
        pass
    
    pass # end of Attributes
        


class ListBox(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onListBox(self) 
