#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


about_msg = """
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                    BBBBB
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

                  DANSE team 
   California Institute of Technology
   (C) 2006-2007 All Rights Reserved
"""



from ControllerBase import ControllerBase

class MainController(ControllerBase):


    def __init__(self, toolkit, gmls):
        self.maingml, self.hellogml = gmls
        self.toolkit = toolkit

        #model
        from models.Friends import Friends
        self.friends = Friends()

        #data
        self.pyshell_locals = {}
        return


    def main(self):

        self.pyshell_locals['controller'] = self
        
        maingml = self.maingml
        toolkit = self.toolkit
        
        self.view = view = toolkit.mainView()
        view.controller = self
        self.pyshell_locals[ 'view' ] = view
        
        from luban.gml import gml2gui
        view = gml2gui( maingml, self, toolkit.renderer() )

        view.start()
        return


    def update(self):
        names = self.friends.keys()
        self.view.getSubview("namelistpanel").update( names )
        return


    def OnAbout(self,e):
        toolkit = self.toolkit
        toolkit.messageDialog( None, "Dummy application", about_msg )
        return


    def OnExit(self, evt):
        self.view.end()
        return


    def OnHello(self, evt):
        from HelloController import HelloController
        helloController = HelloController( self.toolkit, self.hellogml)
        hello = helloController.main()
        if hello is None: return
        name, greetings = hello
        print "%s, %s" % ( greetings, name )
        self.friends[name] = greetings

        self.update()


    def OnListSelectChanged(self, evt):
        print "list select changed"
        return

    
    def OnOpenFile( self, evt ):
        selected = self.toolkit.loadfileDialog(
            None, "Open file" ,
            defaultDir = '.' )
        print selected
        return


    def OnKeyDownInShellWindow(self, evt):
        #check if <enter> is hit
        if evt.getKeyCode() != 13: return

        print "<ENTER>"
        return


    def OnKeyDownInListWindow(self, evt):
        #print evt.getKeyCode()
        if evt.getKeyCode( ) == 127: # delete
            print "<DELETE>"
            pass
        return

    
    pass # end of MainController



import os

# version
__id__ = "$Id$"

# End of file 
