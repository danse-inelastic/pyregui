

class TraitProxy(object):


    def __init__(self, pyre_inventory, pyre_trait):
        self._inv = pyre_inventory
        self._trait = pyre_trait
        return


    def name(self): return self._trait.name


    def type(self): return self._trait.type


    def tip(self): return self.meta( 'tip' ) or ""


    def opacity(self): return self.meta('opacity') or 0


    def importance(self): return self.meta( "importance" ) or 0


    def meta(self, key): return self._trait.meta.get( key )


    def value(self):
        try: return self._trait.__get__( self._inv )
        except Exception, e:
            msg =  "Unable to get value of trait %s from inventory %s\n" % (
                self._trait.name, self._inv._priv_name)
            msg += "Because of %s, %s" % (e.__class__.__name__, e)
            raise ValueError , msg
        raise "should not reach here"


    def setValue(self, value):
        self._trait.__set__( self._inv, value )
        self._trait.meta['gui-configured'] = True
        return


    def valueAsString(self): self._nie("valueAsString")


    def __repr__(self): return "proxy of pyre trait %s" % self.name()


    def _nie(self, method):
        raise NotImplementedError , "%s must provide method %s" % (
            self.__class__.__name__, method)


    pass #end of TraitProxy



def test():
    from pyre.components.Component import Component
    class Inventory(Component.Inventory):

        import pyre.inventory as inv

        a = inv.str('a', default =  'abc' )
        a.meta['tip'] = "a is the first alphabet"
        a.meta['opacity'] = 10

        pass

    inventory = Inventory("i")

    ap = TraitProxy( inventory, Inventory.a )

    assert ap.name() == "a"
    assert ap.value() == "abc"
    assert ap.tip() == Inventory.a.meta['tip']
    ap.setValue( "def" )
    assert ap.value() == "def"
    assert ap.opacity() == 10
    assert ap.importance() == 0
    print "test of TraitProxy passed"
    return


if __name__ == "__main__": test()

