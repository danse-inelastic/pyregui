
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
    


class PropertyBox:

    def __init__(self, parent, property ):
        self.parent = parent
        self.property = property
        self.SetValue( property.value() )
        return


    def SetValue(self, value):
        self.value = value
        return


    def GetValue(self):
        return self.value


    def show(self):
        prompt = "(%s) " % self.GetValue()
        prompt1 = "%s  (%s) " % (self.parent.indentation, self.GetValue())

        save = self.property.value()
        
        toolkit = self.parent.toolkit
        
        while 1:

            candidate = raw_input( prompt )
            if candidate == "": return

            try:
                self.property.setValue( candidate )
                self.value = candidate
                self.property.setValue( save ) #restore
                return
            except Exception, msg:
                toolkit.messageBox( "Invalid input", str(msg) )
                import traceback
                traceback.print_exc(3)
                pass
            prompt = prompt1
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
        facility = self.facility
        indentation = parent.indentation
        promptFmtStr = "\n%s -- Facility '%s', current component '%s'   (configure <c>, use new component <n>, bypass <b>): "
        component = facility.component()
        componentName =  facility.valueAsString()
        save = componentName, component
        
        from pyregui.inventory.proxies.InventoryProxy import DynamicLoadingError

        while 1:
            
            prompt = promptFmtStr % (indentation, facility.name(), componentName )
            action = raw_input(prompt)

            if action == 'b': break
            if action == 'c' or action == '':
                from InventoryDialog import InventoryDialogLoop
                InventoryDialogLoop(parent, component,
                                    parent.toolkit, verbosity = parent.verbosity,
                                    indentLevel = parent.indentLevel+1)
                break
            
            elif action == 'n':
                newComponentName = raw_input( "%s   - name of new component? " % indentation )
                inventory = parent.inventory
                if newComponentName != componentName:
                    #print "set facitity %s to %s" % (facility_name, newComponentName)
                
                    try: 
                        inventory.setFacility( facility.name(), newComponentName )
                        componentName = newComponentName
                        component = facility.component()
                        self.SetValue((componentName,component))
                        self.componentRegistry[ componentName ] = component
                        facility.setValue( save[1] ) #restore
                        
                    except DynamicLoadingError, msg:
                        parent.toolkit.messageBox( str(msg), "Dynamic Loading Error" )
                    pass
                pass
            continue
        return 
