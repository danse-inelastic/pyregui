
from pyregui.guitoolkit.abstract import InputBoxFactory as base

class InputBoxFactory( base ):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def setToolTip( self, guielement, tip ): return


    def register(self, trait, guielement):
        self.parent.registerInputBox( trait, guielement )
        return


    def bindEvtHandler( self, trait, guielement): return


    def onProperty(self, property):
        return PropertyBox( self.parent, property )


    def onFacility(self, facility):
        return FacilityBox( self.parent, facility )
        

    onPropertyWithChoices = onBoolean = onString = onProperty

    pass
    


def traitRepr( trait ):
    name = trait.name()
    tip = trait.tip()
    if tip == '': return "'%s'"%name
    return "'%s', %s" % (name, tip)



class PropertyBox:

    def __init__(self, parent, property ):
        self.parent = parent
        self.property = property
        self.SetValue( property.valueAsString() )
        return


    def SetValue(self, value):
        self.value = value
        return


    def GetValue(self):
        return self.value


    def show(self):
        title = "%s" % (traitRepr( self.property ),)

        save = self.property.value()
        
        toolkit = self.parent.toolkit
        df = toolkit.dlgFactory
        
        while 1:
            value = self.GetValue()
            width = len(value)
            if width < 30: width = 30
            if width > 70: width = 70
            if len(title)/width > 2: width = 70 # title should not be too high
            height = len(title)/width + len(value)/width + 8
                        
            (code, candidate) = df.inputbox(
                title, init=value, width = width, height = height )

            if code in (df.DIALOG_CANCEL, df.DIALOG_ESC): return
            
            try:
                self.property.setValue( candidate )
                self.value = candidate
                self.property.setValue( save ) #restore
                return
            except Exception, msg:
                toolkit.messageBox( "Invalid input", str(msg) )
##                 import traceback
##                 traceback.print_exc(3)
                pass
            continue
        return



class FacilityBox:
    
    def __init__(self,  parent, facility ):
        self.componentRegistry = {}
        self.parent = parent
        self.facility = facility
        component = facility.component()
        compName = facility.valueAsString()
        self.SetValue( (compName, component) )
        return


    def SetValue(self, value):
        compName, component = value
        self.value = compName, component
        self.componentRegistry[ compName ] = component
        return


    def GetValue(self): return self.value


    def show(self):
        parent = self.parent
        toolkit = parent.toolkit
        df = toolkit.dlgFactory
        facility = self.facility
        promptFmtStr = "Facility '%s', current component '%s' "
        choices = [ ('c', 'configure'),
                    ('n', 'use new component'),
                    ]
        
        component = facility.component()
        componentName =  facility.valueAsString()
        save = componentName, component
        
        from pyregui.inventory.proxies.InventoryProxy import DynamicLoadingError

        while 1:

            if facility.fixed(): action = 'c'
            else:
                prompt = promptFmtStr % (facility.name(), componentName )
                code, action = df.menu(
                    prompt,
                    width = 60,
                    choices = choices)

                if code in (df.DIALOG_CANCEL, df.DIALOG_ESC): return
                pass

            if action == 'c' :
                from InventoryDialog import InventoryDialogLoop
                InventoryDialogLoop(parent, component,
                                    parent.toolkit, verbosity = parent.verbosity)
                break
            
            elif action == 'n':
                (code, answer) = df.inputbox("name of new component?", init=componentName)
                if code in (df.DIALOG_CANCEL, df.DIALOG_ESC): continue
                
                newComponentName = answer
                inventory = parent.inventory
                if newComponentName != componentName:
                    #print "set facitity %s to %s" % (facility_name, newComponentName)
                
                    try: 
                        inventory.setFacility( facility.name(), newComponentName )
                        componentName = newComponentName
                        component = facility.component()
                        self.SetValue((componentName,component))
                        facility.setValue( save[1] ) #restore
                        
                    except DynamicLoadingError, msg:
                        parent.toolkit.messageBox( str(msg), "Dynamic Loading Error" )
                    pass
                pass
            continue
        return 
