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
        label = traits.str( 'label', default= "pyShell" )
        locals = traits.str( 'locals', default= "None" )
        keydown_callback = traits.str( 'keydown-callback', default= "None" )
        pass
    
    pass # end of Attributes
        


class PyShell(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onPyShell(self) 
