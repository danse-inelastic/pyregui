
from TraitVisitor import TraitVisitor

class GuiElementFactory(TraitVisitor):


    def __init__(self, parentWindow):
        self.parent = parentWindow
        return


    def postCreation(self, trait, res): self._nie( "postCreation" )


    def createGuiElement(self, trait):
        res = self.dispatch( trait )
        return res


    def __call__(self, trait):
        element = self.createGuiElement(trait)
        self.postCreation(trait, element)
        return element
        

    pass # end of SetButtonFactory
        



