from pyre.component.Component import Component




class TextHolder(Component):
    def __init__(self, name='TextHolder', facility='TextHolder'):
        Component.__init__(self, name, facility)
        self.type = "textholder"
        return
    
    def setText(self, text):
        self.text = text
        return