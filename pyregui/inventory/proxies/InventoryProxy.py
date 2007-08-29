

from FacilityProxy import DynamicLoadingError

class InventoryProxy( object ):


    ignored_props = ["typos", "help-persistence", "help", "help-properties", "help-components"]
    ignored_facs  = ["weaver", "journal"]
    

    def __init__(self, pyre_inventory):
        inv = self._inv = pyre_inventory
        from PropertyProxy import PropertyProxy
        from FacilityProxy import FacilityProxy
        from pyre.inventory.Property import Property

        #print "InventoryProxy.__init__"

        #print "--properties:"
        propProxies = {}
        for prop in inv.properties():
            if prop.name in self.ignored_props: continue
            if isinstance(prop, Property):
                #print "  %s" % prop.name
                proxy = PropertyProxy( inv, prop )
                propProxies[proxy.name()] = proxy
                pass
            continue

        #print "--facilities"
        facProxies = {}
        for fac in inv.facilities():
            if fac.name in self.ignored_facs: continue
            #print "  %s" % fac.name
            proxy =  FacilityProxy( inv, fac ) 
            facProxies[ proxy.name() ] = proxy
            continue
            
        self._pps = propProxies
        self._fps = facProxies

        #print "InventoryProxy.__init__: done"
        return


    def name(self): return self._inv._priv_name


    def properties(self, verbosity = 1):
        res = []
        for prop in self._pps.values():
            if prop.opacity() < verbosity: res.append( prop )
        return res


    def facilities(self, verbosity = 1): 
        res = []
        for fac in self._fps.values():
            if fac.opacity() < verbosity: res.append( fac )
        return res


    def traits(self, verbosity = 1):
        res = self.properties(verbosity = verbosity) + self.facilities(verbosity = verbosity)
        res.sort( lambda x,y: y.importance() - x.importance() )
        return res


    def propertyNames(self, verbosity = 1):
        return [ prop.name() for prop in self.properties( verbosity ) ]


    def facilityNames(self, verbosity = 1): 
        return [ fac.name() for fac in self.facilities( verbosity ) ]


    def getValueAsString(self, traitName):
        if traitName in self._pps.keys(): return self._pps[traitName].valueAsString()
        if traitName in self._fps.keys(): return self._fps[traitName].valueAsString()
        return


    def notifyObservers(self):
        '''If the inventory has an extension to support observers, call
        the notify method'''
        inv = self._inv
        if not hasattr(inv, 'notifyObservers'): return
        inv.notifyObservers()
        return
    

    def property(self, name):
        "return proxy of pyre inventory property with given name"
        return self._pps[ name ]


    def facility(self, name):
        "return proxy of pyre inventory facility with given name"
        return self._fps[name]
    

    def setProperty(self, propertyName, value):
        self._pps[ propertyName ].setValue( value )
        return


    def setFacility(self, facilityName, componentName):
        self._fps[facilityName].setDynamicComponent( componentName )
        return


    def getComponent(self, facilityName):
        return self._fps[facilityName].component()


    def getComponentInventory(self, facilityName):
        return self._fps[facilityName].component().inventory


    pass # end  of class InventoryProxy




def test():
    from pyre.components.Component import Component

    class Sin(Component):

        def __init__(self, name = "Sin", facility = "func"):
            Component.__init__(self, name, facility)
            return
        
        pass #end of class Sin
    
    
    #following test requres Cos.odb
    import os
    if not (os.path.exists("Cos.odb") and os.path.isfile("Cos.odb")):
        raise "This test needs file 'Cos.odb'"

    from pyre.applications.Script import Script
    class TestApp(Script):

        class Inventory(Script.Inventory):
            import pyre.inventory as inv
            s = inv.str('s', default = "abc")
            i = inv.int('i', default = 10 )
            f = inv.float('f', default = 3.0)
            func = inv.facility( "func", factory = Sin)
            pass

        def __init__(self, name = "TestApp"):
            Script.__init__(self, name)
            return


        def main(self, *args, **kwds):
            invp = InventoryProxy( self.inventory )
            assert compareList( invp.getPropertyNames(),  ['typos', 'i', 's', 'f'] )
            assert compareList( invp.getFacilityNames(),  ['func'] )
            
            #print "properties:"
            for propName in invp.getPropertyNames():
                #print "\t%s=%s" % (propName, invp.getValueAsString( propName ) )
                continue
            
            #print "facilities:"
            for facName in invp.getFacilityNames():
                #print "\t%s=%s" % (facName, invp.getValueAsString( facName ) )
                continue

            invp.setProperty( "i", "300" )
            assert invp.getValueAsString( "i" ) == "300"

            try: invp.setProperty( "i", "33.3" )
            except ValueError: pass

            invp.setFacility( "func", "Cos" )
            assert invp.getComponent( "func" ).__class__.__name__ == "Cos"
            cosInv = invp.getComponentInventory( "func" )
            from pyre.inventory.Inventory import Inventory
            assert isinstance( cosInv, Inventory )
            return
            
        pass # end of class TestApp

    test = TestApp()
    test.run()

    print "test of InventoryProxy passed"
    return


def compareList(a,b):
    """a==b: return True
    a!=b: return False
    """
    for ia in a:
        if not ia in b: return False
        continue

    for ib in b:
        if not ib in a: return False
        continue

    return True


if __name__ == "__main__": test()
