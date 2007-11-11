from pyre.components.Component import Component

class TextHolder(Component):
    def __init__(self, name='TextHolder', facility='TextHolder'):
        Component.__init__(self, name, facility)
        self.type = "textholder"
    
    def setText(self, text):
        self.text = text
    
#from pyre.inventory.properties.String import String
#
#class TextHolder(String):
#    def __init__(self, name, **kwds):
#        String.__init__(self, name, **kwds)
#        self.type = "textholder"
#
#    def setText(self, text):
#        self.text = text
