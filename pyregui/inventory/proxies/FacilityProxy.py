import journal
debug = journal.debug( 'pyregui.inventory.proxies' )

class DynamicLoadingError( Exception ) : pass


from TraitProxy import TraitProxy

class FacilityProxy(TraitProxy):


    def __init__(self, pyre_inventory, pyre_facility):
        TraitProxy.__init__(self, pyre_inventory, pyre_facility)
        return


    def fixed(self): return self.meta('fixed')


    def known_plugins(self): return self.meta('known_plugins') or []


    def valueAsString(self):
        component = self.component()
        name = component.name
        debug.log(  "FacilityProxy: %s, id=%s, component=%r" % (name, id(component), component) )
        return component.name


    def component(self):
        comp = self.value()
        if comp is None: raise "Unable to get component of facility %s" % self.name()
        return comp


    def setDynamicComponent(self, name):
        "load component from a odb file identified by its file name"
        self.setValue( name )
        if self.valueAsString() != name:
            raise DynamicLoadingError, "Unable to load component %s" % name
        self._inv.configureComponents()
        return


    pass # end of FacilityProxy




def test():
    from pyre.components.Component import Component

    class Sin(Component):

        def __init__(self, name = "Sin", facility = "func"):
            Component.__init__(self, name, facility)
            return
        
        pass #end of class Sin
    
    
    class Inventory(Component.Inventory):

        import pyre.inventory as inv

        func = inv.facility('func', factory = Sin )

        pass

    inventory = Inventory("i")

    funcp = FacilityProxy( inventory, Inventory.func )

    assert funcp.name() == "func"
    assert isinstance( funcp.value(), Sin )
    assert isinstance( funcp.component(), Sin )
    assert funcp.valueAsString() == "Sin"


    #following test requres Cos.odb
    import os
    if not (os.path.exists("Cos.odb") and os.path.isfile("Cos.odb")):
        raise "This test needs file 'Cos.odb'"
    TestInv = Inventory
    from pyre.applications.Script import Script
    class TestApp(Script):

        class Inventory(Script.Inventory, TestInv):
            pass

        def __init__(self, name = "TestApp"):
            Script.__init__(self, name)
            return


        def main(self, *args, **kwds):
            funcp = FacilityProxy( self.inventory, self.Inventory.func )
            funcp.setDynamicComponent("Cos")
            assert type(self.inventory.func).__name__ == "Cos"
            try: funcp.setDynamicComponent("bbb")
            except DynamicLoadingError: pass
            else: raise "expect DynamicLoadingError"
            return
            
        pass # end of class TestApp

    test = TestApp()
    test.run()

    print "test of FacilityProxy passed"
    return


if __name__ == "__main__": test()

