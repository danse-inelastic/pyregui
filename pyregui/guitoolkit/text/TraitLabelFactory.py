
from pyregui.guitoolkit.abstract import TraitLabelFactory as base

class TraitLabelFactory( base ):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def postCreation(self, trait, element): return


    def onProperty(self, property):
        return PropertyLabel("%s: " % traitRepr( property ) )

    def onFacility(self, facility):
        return FacilityLabel("%s: " % traitRepr( facility ) )

    onPropertyWithChoices = onBoolean = onString = onProperty 

    pass


def traitRepr( trait ):
    name = trait.name()
    tip = trait.tip()
    if tip == '': return "'%s'"%name
    return "'%s', %s" % (name, tip)


class PropertyLabel:

    def __init__(self, text):
        self.text = text
        return

    def show(self):
        print "* %s" % self.text,
        return
    

class FacilityLabel:

    def __init__(self, text):
        self.text = text
        return

    def show(self):
        print "+ %s" % self.text,
        return
    
