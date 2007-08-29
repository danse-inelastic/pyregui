#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                   (C) Copyright 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## This visitor creates the "set" button for the given trait of a pyre inventory


import webhelpers as wh

from pyregui.inventory.proxies.InventoryProxy import DynamicLoadingError


from pyregui.guitoolkit.abstract.SetButtonFactory import SetButtonFactory as Base


class SetButtonFactory(Base):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def postCreation(self, trait, guielement):
        return


    def nobutton(self, trait):
        return ''


    onPropertyWithChoices = onBoolean = onString = onProperty = nobutton


    def onFacility(self, fac):
        currentInventoryUrl = self.parent.currentInventoryUrl
        appname = self.parent.appname

        name = fac.name()
        url = '/'.join( [currentInventoryUrl, name] )

        return '<input type="submit" value="Set" name="set%s" />' % name
##         b = wh.button_to(
##             "Set", url = wh.url( appname = appname, todo = "set", url = url ) )
        return b


    def oninputfile(self, prop):
        name = prop.name()
        b = '<input type="submit" value="Browse" name="set%s" />' % name
        return b


    def onoutputdir(self, prop):
        name = prop.name()
        b = '<input type="submit" value="Browse" name="set%s" />' % name
        return b
        

    def createGuiElement(self, trait):
        special_props = ['inputfile', 'outputdir']
        
        from pyregui.inventory.proxies.PropertyProxy import PropertyProxy
        
        type = trait.type()
        
        if isinstance( trait, PropertyProxy ) and type in special_props:
            return getattr(self, 'on%s' % type)( trait )
        
        return Base.createGuiElement(self, trait)


    pass # end of SetButtonFactory
        


# version
__id__ = "$Id$"

# End of file 
