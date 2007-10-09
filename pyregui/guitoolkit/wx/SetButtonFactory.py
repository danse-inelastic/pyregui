
import wx
from pyregui.inventory.proxies.InventoryProxy import DynamicLoadingError
from pyregui.guitoolkit.wx.LargeTextLoader import LargeTextLoader


from pyregui.guitoolkit.abstract.SetButtonFactory import SetButtonFactory as Base

class SetButtonFactory(Base):

    def __init__(self, parentWindow):
        self.parent = parentWindow
        return

    def postCreation(self, trait, guielement):
        return

    def nobutton(self, trait):
        return

    onPropertyWithChoices = onBoolean = onString = onProperty = nobutton

    def onFacility(self, fac):
        b = wx.Button(self.parent, label="Set")
        self.parent.Bind(wx.EVT_BUTTON, self.SetChosenComponent( fac ),  b)
        self.parent.registerGuiElement( "setButton", fac, b)
        b.SetToolTipString( "configure details of '%s': %s" % (
            fac.name(), fac.tip() ) )
        return b

    def onInputfile(self, prop):
        b = wx.Button(self.parent, label="Choose")
        self.parent.Bind(wx.EVT_BUTTON, self.ChooseFile( prop ),  b)
        b.SetToolTipString( "choose file for %s from browser" % prop.tip())
        return b

    def onOutputDir(self, prop):
        b = wx.Button(self.parent, label="Choose")
        self.parent.Bind(wx.EVT_BUTTON, self.ChooseDir( prop ),  b)
        b.SetToolTipString( "choose directory for %s from browser" % prop.tip())
        return b
    
    def onLargeTextLoad(self, fac):
        b = wx.Button(self.parent, label="Set")
        self.parent.Bind(wx.EVT_BUTTON, self.SetLargeText( fac ),  b)
        b.SetToolTipString( "input atomic information")
        return b    
    

    def ChooseFile(self, prop):
        import os
        def _(event):
            v = self.parent.getUserInput( prop )
            default = os.path.split( v )[0]
            if len(default) == 0: default = '.'
            d = wx.FileDialog( self.parent, "Select input file for %s: %s" % (
                prop.name(), prop.tip() ), defaultDir = default )
            if d.ShowModal() != wx.ID_OK: d.Destroy(); return
            res = str(d.GetPath())
            d.Destroy()
            self.parent.setUserInput( prop, res )
        return _


    def ChooseDir(self, prop):
        def _(event):
            default = self.parent.getUserInput( prop )
            if len(default ) == 0: default = '.'
            res = wx.DirSelector(
                "Select output directory", 
                defaultPath = default )
            if res is None or res == '': res = '.'
            self.parent.setUserInput( prop, res )
        return _

    
    def SetLargeText(self, fac):
        # eventually this can be generalized to load any multiline text 
        # for now, however, it only calls the setAtoms method of AtomLoader in UnitCellBuilder.py
        def _(event):
             dialog = LargeTextLoader( self.parent)
             if dialog.ShowModal() == wx.ID_OK:
                 component = fac.getComponent()
                 component.setAtoms( dialog.getText() )
            #newComponentName = self.parent.getUserInput( facility )
            #print "new component name", newComponentName
            #inventory = self.parent.inventory
#            if newComponentName != inventory.getValueAsString( facility.name() ):
#                #print "set facitity %s to %s" % (facility_name, newComponentName)
#                try: 
#                    inventory.setFacility( facility.name(), newComponentName )
#                except DynamicLoadingError, msg:
#                    wx.MessageBox( str(msg), "Dynamic Loading Error" )
#                    return
#            #print "get pyre component of facility %s" % facility_name
#            pyre_component = inventory.getComponent( facility.name() )
#            toolkit = self.parent.toolkit
#            return toolkit.InventoryDialogLoop( self.parent, pyre_component, toolkit )
        return _
    

    def SetChosenComponent( self, facility ):
        def _(event):
            newComponentName = self.parent.getUserInput( facility )
            #print "new component name", newComponentName
            inventory = self.parent.inventory
            if newComponentName != inventory.getValueAsString( facility.name() ):
                #print "set facitity %s to %s" % (facility_name, newComponentName)
                try: 
                    inventory.setFacility( facility.name(), newComponentName )
                except DynamicLoadingError, msg:
                    wx.MessageBox( str(msg), "Dynamic Loading Error" )
                    return
            #print "get pyre component of facility %s" % facility_name
            pyre_component = inventory.getComponent( facility.name() )
            toolkit = self.parent.toolkit
            return toolkit.InventoryDialogLoop( self.parent, pyre_component, toolkit )
        return _
    


    def createGuiElement(self, trait):
        from pyregui.inventory.proxies.PropertyProxy import PropertyProxy
        if isinstance( trait, PropertyProxy ):
            if trait.type() == "inputfile" : return self.onInputfile( trait )
            if trait.type() == "outputdir" : return self.onOutputDir( trait )
        else:
            if trait.name() == "Atomic/Species information" : return self.onLargeTextLoad( trait )
            pass
        
        return Base.createGuiElement(self, trait)
    
        
    pass # end of SetButtonFactory
        



