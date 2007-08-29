

class TraitVisitor:

    def onPropertyWithChoices(self, prop): self._nie( "onPropertyWithChoices" )

    def onBoolean(self, prop): self._nie( "onBoolean" )

    def onString(self, prop): self._nie( "onString" )

    def onProperty(self, prop): self._nie( "onProperty" )

    def onFacility(self, fac): self._nie( "onFacility" )


    def _nie(self, method):
        raise NotImplementedError , "%s must override %s" % (
            self.__class__.__name__, method )


    def dispatch(self, trait):
        from pyregui.inventory.proxies.FacilityProxy import FacilityProxy
        from pyregui.inventory.proxies.PropertyProxy import PropertyProxy
        from pyre.inventory.validators import Range, Choice
        if isinstance( trait, PropertyProxy ):
            prop = trait
            ptype =  prop.type()
            validator =  prop.validator() 
            if type(validator) == Choice.Choice:
                res = self.onPropertyWithChoices( prop )
            elif ptype == 'bool':
                res = self.onBoolean( prop )
            elif ptype == 'str':
                res = self.onString( prop )
            else:
                res = self.onProperty( prop )
                pass
            pass
        else:
            res = self.onFacility( trait )
            pass
        return res


    pass # end of SetButtonFactory
        



