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


## This visitor creates a input box (text field) for the given trait of
## a pyre inventory


from pyregui.guitoolkit.abstract import InputBoxFactory as base
import webhelpers as  wh


class InputBoxFactory( base ):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def register(self, trait, inputBox): return


    def bindEvtHandler(self, trait, inputBox): return
    

    def setToolTip( self, guielement, tip ): return


    def onPropertyWithChoices(self, prop):
        validator = prop.validator()
        choices = map(str, validator.value)
        return self.onChoices( prop, choices )
    

    def onBoolean(self, prop):
        return self.onChoices( prop, ["True", "False"] )
    

    def onString(self, prop): 
        alts = prop.known_alternatives()
        if alts:
            res = self.onChoices( prop, alts )
        else:
            res = self.onProperty( prop )
        return res


    def onChoices(self, trait, choices):
        name = trait.name()
        default = trait.valueAsString()
        options = wh.options_for_select( choices, default )
        res = wh.select( name, options )
        return res
    

    def onProperty(self, prop):
        name = prop.name()
        default = prop.valueAsString()
        res = wh.text_field( name, default )
        return res
    

    def onFacility(self, fac):
        parent = self.parent
        choices = fac.known_plugins()
        current_choice = fac.valueAsString()
        if current_choice not in choices: choices.append( current_choice )
        options = wh.options_for_select( choices, current_choice )
        name = fac.name()
        res = wh.select( name, options )
        return res


    pass
    


def traitRepr( trait ):
    name = trait.name()
    tip = trait.tip()
    if tip == '': return "'%s'"%name
    return "'%s', %s" % (name, tip)




# version
__id__ = "$Id$"

# End of file 
