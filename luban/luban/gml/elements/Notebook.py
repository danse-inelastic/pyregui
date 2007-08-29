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
        borderStyle = traits.str('borderStyle', default="sunken" )
        titles = traits.list('titles', default = [])
        pass
    
    pass # end of Attributes
        

from Element import Element

class Notebook(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onNotebook(self) 

    pass # end of Notebook



