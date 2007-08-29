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


def _intlist( input ): return [ int(i) for i in input ]


class Attributes(AttributeInventory):
    
    class Inventory( AttributeInventory.Inventory ):

        import traits
        size = traits.list('size', default=[4,3], validator = _intlist)
        dpi = traits.int('dpi', default=75)
        label = traits.str('label', default='thelabel')
        pass
    
    pass # end of Attributes
        

class HistogramFigure(Element):

    AttributeContainer = Attributes

    def identify(self, visitor): return visitor.onHistogramFigure(self) 

    pass # end of HistogramFigure



