

from pyregui.guitoolkit.abstract.InputBoxFactory import InputBoxFactory as Base

import wx

class InputBoxFactory(Base):

    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def register(self, trait, inputBox):
        self.parent.registerInputBox( trait, inputBox )
        return


    def bindEvtHandler(self, trait, inputBox):
        wx.CallAfter(inputBox.SetInsertionPoint, 0)
        return
    

    def setToolTip(self, ctrl, tip):
        ctrl.SetToolTipString( tip )
        return
    

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
        parent = self.parent
        if len(choices) == 1:
            res = wx.TextCtrl(
                parent, -1, trai.valueAsString(), (90,50), (200,-1 )
                )
        else:
            res = wx.ComboBox(
                parent, -1, trait.valueAsString(), (90, 50), (200,-1), choices
                )
            pass
        return res
    

    def onProperty(self, prop):
        parent = self.parent
        res = wx.TextCtrl(parent, -1, prop.valueAsString(), (90, 50), (200,-1))
        return res
    

    def onFacility(self, fac):
        parent = self.parent
        choices = fac.known_plugins()
        current_choice = fac.valueAsString()
        if current_choice not in choices: choices.append( current_choice )

        if len(choices) == 1:
            res = wx.TextCtrl(
                parent, -1, current_choice, (90,50), (200,-1 )
                )
        else:
            #drop down list
            res = wx.ComboBox(
                parent, -1, current_choice, (90,50), (200,-1),
                choices,
                wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
            pass
        return res


    pass # end of InputBoxFactory
        

