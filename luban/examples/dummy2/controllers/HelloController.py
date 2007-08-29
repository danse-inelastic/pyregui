#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ControllerBase import ControllerBase

class HelloController(ControllerBase):

    def __init__(self, toolkit, hellogml):

        self.toolkit = toolkit
        self.hellogml = hellogml
        
        return


    def main(self):
        from luban.View import View
        view = View()
        self.view = view

        from luban.gml import gml2gui
        hellogml = self.hellogml
        view = gml2gui( hellogml, self, self.toolkit.renderer() )
        
        dialog = view.getSubview( 'hellodialog' )
        dialog.show()

        ret = None
        
        if dialog.ok():
            name = view.getSubview('namefield').value()
            greetings = view.getSubview('greetingsfield').value()
            ret = name, greetings
            pass
        
        dialog.destroy()

        return ret
        


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Sat Jul 21 07:21:44 2007

# End of file 
