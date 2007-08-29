

from pyregui.inventory.proxies.InventoryProxy import InventoryProxy


def InventoryDialogLoop( parent, pyre_component, toolkit, verbosity = 1):

    InventoryDialog = toolkit.InventoryDialog
    dlg = InventoryDialog(
        parent = parent,
        pyre_component = pyre_component,
        pyre_inventory = pyre_component.inventory,
        verbosity = verbosity, toolkit = toolkit)

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
            if newComponent != fac.value(): fac.setValue( newComponent )
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

    spacer = "====="

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
        toolkit = self.toolkit
        df = toolkit.dlgFactory

        while 1:
            (code, tag) = df.menu(
                self.dlgTitle,
                width=70, item_help = 1,
                choices=self.choices)
            
            if code in (df.DIALOG_CANCEL, df.DIALOG_ESC): return toolkit.ID_CANCEL

            if tag == self.spacer: continue
            if tag == "*Done": break
            traitName = tag
            inputBox = self.getGuiElement( "inputBox", traitName )
            inputBox.show()
            continue
        return toolkit.ID_OK


    def Destroy(self): return


    def __init__(
        self, parent = None,
        pyre_component = None, pyre_inventory = None,
        verbosity = 1, toolkit = None,
        ):

        self.parent = parent

        self.toolkit = toolkit

        self._registry = GuiElementRegistry()
        
        self.inputBoxFactory = self.toolkit.InputBoxFactory(self)
        self.setButtonFactory = self.toolkit.SetButtonFactory(self)
        self.labelFactory = self.toolkit.TraitLabelFactory(self)

        self.inventory = InventoryProxy(pyre_inventory)
        self.pyre_component = pyre_component
        self.verbosity = verbosity

        self.dlgTitle = "Settings of '%s'" % pyre_component.name
        #self.dlgTitle += "\n When done, type <*> and then <enter>"

        if pyre_component.__class__.__doc__ is not None:
            docstr = pyre_component.__class__.__doc__
        else:
            docstr = "Please consider writing a docstring for %s" % pyre_component.__class__

        self.choices = []
        self.get_action_window()
        return


    def addEntry( self, trait):
        from pyregui.inventory.proxies.PropertyProxy import PropertyProxy
        from pyregui.inventory.proxies.FacilityProxy import FacilityProxy
        guihint = "<Enter>-OK to change settings, <Enter>-Cancel or <ESC> to cancel"
        self.choices.append( (trait.name(), trait.tip(), guihint) )
        self.inputBoxFactory( trait )
        return


    def get_action_window(self):
        
        traits = self.inventory.traits( verbosity = self.verbosity )
        toolkit = self.toolkit

        for trait in traits: self.addEntry( trait )

        if len(traits):
            self.choices.append( (self.spacer,"====================",'') )
        self.choices.append(
            ("*Done", "finish configuration",
             '<Enter>-OK to use new settings, <Enter>-Cancel or <ESC> to restore'
             ) )

        return 


    # end of class InventoryDialog



