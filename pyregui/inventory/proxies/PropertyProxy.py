#!/usr/bin/env python

from TraitProxy import TraitProxy

class PropertyProxy(TraitProxy):

    def __init__(self, pyre_inventory, pyre_property):
        TraitProxy.__init__(self, pyre_inventory, pyre_property)
        return


    def valueAsString(self): return str(self.value())


    def known_alternatives(self):
        return self._trait.meta.get('known_alternatives') or []
    

    def validator(self):
        if hasattr(self._trait, 'validator'):
            return self._trait.validator
        else:
            return None
        

    pass # end of PropertyProxy




def test():
    from pyre.components.Component import Component
    import pyre.inventory as inv
    
    class Inventory(Component.Inventory):

        a = inv.str('a', default =  'abc' )

        b = inv.float('b', default = 3.0, validator = inv.greater(0) )

        pass

    inventory = Inventory("i")

    ap = PropertyProxy( inventory, Inventory.a )

    assert ap.name() == "a"
    assert ap.value() == "abc"
    ap.setValue( "def" )
    assert ap.value() == "def"

    assert ap.valueAsString() == "def"

    bp = PropertyProxy( inventory, Inventory.b )
    try: bp.setValue( 'a' )
    except ValueError: pass

    assert isinstance( bp.validator(), inv.validators.Greater.Greater )

    print "test of PropertyProxy passed"
    return


if __name__ == "__main__": 
    test()

# end of file

