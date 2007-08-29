

from GuiElementFactory import GuiElementFactory


class InputBoxFactory(GuiElementFactory):
    

    def setToolTip( self, guielement, tip ): self._nie( "setToolTip" )


    def register(self, trait, guielement): self._nie("register")


    def bindEvtHandler( self, trait, guielement): self._nie("bindEvtHandler")
    

    def postCreation(self, trait, guielement):
        self.setToolTip( guielement, trait.tip() )
        self.register( trait, guielement )
        self.bindEvtHandler( trait, guielement )
        return guielement

    pass # end of InputBoxFactory
        



