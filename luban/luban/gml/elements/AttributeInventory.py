#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractAttributeContainer import AbstractAttributeContainer

import traits

class AttributeInventory( AbstractAttributeContainer):

    class Inventory(traits.Inventory):
        pass

    def get( self, name):
        """get( name) -> value"""
        inv = self.inventory
        return inv.getTrait(name).__get__( inv )
    

    def set( self, name, value):
        """set( name, value) -> None"""
        inv = self.inventory
        inv.getTrait(name).__set__( inv, value )
        return
    

    def __init__( self, attributes = None):
        if attributes is None: attributes = {}
        name = attributes.get('name')
        if name is None: name = "name"
        self.inventory = self.Inventory(name)
        for key, value in attributes: self.set( key, value)
        return


    def __iter__(self): return self.inventory.propertyNames().__iter__()


    pass # end of AttributeInventory

    
def test():

    from AbstractAttributeContainer import TestCase as TC

    class TestCase(TC):

        def setUp(self):
            class C(AttributeInventory):
                class Inventory(AttributeInventory.Inventory):
                    hello = traits.int( "hello", default = 1)
                    pass
                pass
            self.attributeContainer = C( "c" )
            return

        pass

    import unittest as ut
    suite = ut.makeSuite( TestCase )
    alltests = ut.TestSuite( (suite, ) )
    ut.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__": test()


# version
__id__ = "$Id$"

# End of file 
