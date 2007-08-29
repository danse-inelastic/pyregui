from pyregui.inventory.proxies.InventoryProxy import InventoryProxy


def InventoryDialogLoop( parent, pyre_component, toolkit, verbosity = 1, indentLevel = 0 ):

    InventoryDialog = toolkit.InventoryDialog
    dlg = InventoryDialog(
        parent = parent,
        pyre_component = pyre_component,
        pyre_inventory = pyre_component.inventory,
        verbosity = verbosity, toolkit = toolkit, indentLevel = indentLevel)

    while 1:

        result = dlg.ShowModal()
        if result != toolkit.ID_OK : break

        error = False
    
        inventory = InventoryProxy(pyre_component.inventory)
        
        for prop in inventory.properties(verbosity = verbosity):
            newValue = dlg.getUserInput( prop )
            inventory.setProperty( prop.name(), newValue )
            continue

        for fac in inventory.facilities(verbosity = verbosity):
            newName, newComponent = dlg.getUserInput( fac )
            fac.setValue( newComponent )
            continue

        if not error: break

        continue
    
    dlg.Destroy()
    print
    return result




class GuiElementRegistry(object):

    def register(self, category, trait, element ):
        if not isinstance(trait, str): trait = trait.name()
        
        if self._reg.get(category) is None: self._reg[category] = {}
        self._reg[category][trait] = element
        return


    def get(self, category, trait):
        if not isinstance(trait, str): trait = trait.name()
        return self._reg[category][trait]


    def __init__(self):
        self._reg = {}
        return


    def __repr__(self):
        return str(self._reg)

    pass



class InventoryDialog:

    indent = '  '

    def registerInputBox( self, trait, box ):
        self._registry.register( "inputBox", trait, box )
        return


    def getUserInput( self, trait ):
        inputBox = self._registry.get( "inputBox", trait )
        return inputBox.GetValue()


    def setUserInput( self, trait, value):
        inputBox = self._registry.get( "inputBox", trait )
        inputBox.SetValue( value )
        return


    def getGuiElement( self, category, trait):
        return self._registry.get(category, trait )


    def registerGuiElement(self, category, trait, element):
        self._registry.register( category, trait, element)
        return


    def ShowModal(self):
        name = self.pyre_component.name
        print
        print
        title = "Configuration report of %s" % name
        print self.indentation, '='*len(title)
        print "%s %s" % (self.indentation, title)
        self.printConfiguration()
        print self.indentation, '='*len(title)
##         print "%s configuration of %s done." % (
##             self.indentation, self.pyre_component.name)
        print
        ok = raw_input ( "%s   OK <y>   or   Cancel <n>: " % self.indentation)
        print
        if ok == 'y':
            print "%s Configuration accepted  :)" % self.indentation
            return self.toolkit.ID_OK
        else:
            print "%s Canceled  :(" % self.indentation
            return self.toolkit.ID_CANCEL
        raise


    def printConfiguration(self):
        traits = self.inventory.traits( verbosity = self.verbosity )
        for trait in traits:
            value = self.getUserInput( trait )
            print "%s * %s: %s" % (self.indentation, trait.name(), value )
            continue
        if len(traits) == 0: print "%s * Nothing configurable" % self.indentation
        return
    

    def Destroy(self): return


    def __init__(
        self, parent = None,
        pyre_component = None, pyre_inventory = None,
        verbosity = 1, toolkit = None,
        indentLevel = 0
        ):
        self.indentLevel = indentLevel
        self.indentation = indentation = self.indent * self.indentLevel

        self.parent = parent

        self.toolkit = toolkit

        self._registry = GuiElementRegistry()
        
        self.inputBoxFactory = self.toolkit.InputBoxFactory(self)
        self.setButtonFactory = self.toolkit.SetButtonFactory(self)
        self.labelFactory = self.toolkit.TraitLabelFactory(self)

        self.inventory = InventoryProxy(pyre_inventory)
        self.pyre_component = pyre_component
        self.verbosity = verbosity

        apptitle = "Configure '%s'" % pyre_component.name

        print indentation, '='*len(apptitle)
        print indentation, apptitle
        print indentation, '='*len(apptitle)

        if pyre_component.__class__.__doc__ is not None:
            docstr = pyre_component.__class__.__doc__
        else:
            docstr = "Please consider writing a docstring for %s" % pyre_component.__class__

        self.get_action_window()
        return


    def get_action_window(self):
        
        traits = self.inventory.traits( verbosity = self.verbosity )
        toolkit = self.toolkit
        sizer = toolkit.GridSizer( 3, len(traits) )

        row = 1
        for trait in traits:
            print self.indentation,
            l = self.labelFactory( trait ); sizer.Add( l, pos=(row, 0) )
            t = self.inputBoxFactory( trait ); sizer.Add( t, pos=(row, 1))
##             b = self.setButtonFactory( trait )
##             if b: sizer.Add(b, pos = (row, 2) )
            row = row+1
            continue

        return sizer


    # end of class InventoryDialog



