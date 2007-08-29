
import wx

from pyregui.guitoolkit.abstract import TraitLabelFactory as base

class TraitLabelFactory( base ):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def postCreation(self, trait, element): return


    def onTrait(self, trait):
        invDialog = self.parent
        #text = trait.tip()
        #if len(text) == 0: text = trait.name()
        text = trait.name()
        s = "%s" % (text,)
        res = wx.StaticText(invDialog, -1, s)
        res.SetToolTipString( trait.tip() )
        return res

    onPropertyWithChoices = onBoolean = onString = onProperty = onFacility = onTrait

    pass
    
