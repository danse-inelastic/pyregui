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


## This visitor creates a label for the given trait of a pyre inventory

import wx

from pyregui.guitoolkit.abstract import TraitLabelFactory as base

class TraitLabelFactory( base ):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def postCreation(self, trait, element): return


    def onTrait(self, trait):
        return "<p>%s</p>" % trait.tip()

    onPropertyWithChoices = onBoolean = onString = onProperty = onFacility = onTrait

    pass
    

# version
__id__ = "$Id$"

# End of file 
