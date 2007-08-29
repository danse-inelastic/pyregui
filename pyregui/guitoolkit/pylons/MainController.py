#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                   (C) Copyright 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# This is the main controller.


from SetButtonFactory import SetButtonFactory
from InputBoxFactory import InputBoxFactory
from TraitLabelFactory import TraitLabelFactory


import os
open_default_inputfile = os.path.expanduser( '~' )


class MainController:

    project_lib_base = None # overload this when install this to different pylons project


    def __init__(self):
        return


    def index(self, appname, todo=None, url = ''):
        "main dispatcher"
        plb = self.project_lib_base
        
        environ = plb.request.environ
        remote_addr = environ.get('REMOTE_ADDR')
        if  remote_addr != "127.0.0.1": 
            raise "only local connection is allowed: %s" % remote_addr

        print self.get_controller_name(), appname, todo, url

        if appname is None or len(appname) == 0:
            return self.listApps()
        
        self.curlink= '/'.join( ['', appname, todo or '', url or '' ] )

        self.appname = appname
        self.todo = todo
        self.url = url
        
        if todo is None: return self.main(appname)

        if url is None: url = ''
        self.currentInventoryUrl = url

        return getattr( self, todo)( url )


    def render_response(self, template):
        raise NotImplementedError


    def listApps(self):
        plb = self.project_lib_base
        c = plb.c
        c.controller = self
        from pyreapp_registry import registry
        c.pyreapp_registry = registry
        template = "pyregui/listapp.myt"
        return self.render_response( template )


    def setProperty(self, url):
        """handles :controller/:appname/setProperty/:path_to_property
        set property to new value returned from property set dialog
        """
        app = self.get_app( self.appname )
        print self.get_controller_name(), "setProperty", url
        property = find_property( app, url )
        from PropertySetter import PropertySetter
        self.propertySetter = PropertySetter(self)
        return self.propertySetter( property )
    

    def setInventory(self, url ):
        """handles :controller/:appname/setInventory/:path_to_inventory
        This method is called when a button in the configuration form
        is pressed.
        """
        app = self.get_app( self.appname )
        plb = self.project_lib_base

        inventory = find_inventory( app, url )

        #result from configuration form are stored in params
        params = plb.request.params

        # canceled
        Cancel = params.get( "Cancel" )
        if Cancel :
            self._restore_configuration_from_session( inventory )
            pass

        else:
            # set new values for each inventory item
            for trait in inventory.traits():
                name = trait.name()
                value = params.get( name )
                if trait.valueAsString() != str(value): trait.setValue( value )
                continue

            # see if a "set" button is pressed
            from pyregui.inventory.proxies.PropertyProxy import PropertyProxy
            from pyregui.inventory.proxies.FacilityProxy import FacilityProxy

            from PropertySetResponder import PropertySetResponder
            self.propertySetResponder = PropertySetResponder(self)

            for trait in inventory.traits():
                name = trait.name()
                set = params.get( 'set%s' % name )

                if set:
                    if isinstance( trait, FacilityProxy ):
                        #go deeper in inventory
                        newurl = '/'.join( [url, name] )
                        return plb.h.redirect_to(
                            todo = "configure", url = newurl ) 

                    elif isinstance(trait, PropertyProxy):
                        return self.propertySetResponder( trait )
                    else:
                        raise NotImplementedError
                    pass

                continue

            # if we reach here,
            # OK must be pressed
            OK = params.get( 'OK' )
            if not OK: raise "interior logic error"
            pass

        if len(url) == 0: # we are on the top level configuration panel
            return plb.redirect_to( todo=None )

        components = url.split('/')

        newurl = '/'.join( components[:-1] )
        return plb.redirect_to( todo='configure', url = newurl )


    def configure(self, url):
        """handles :controller/:appname/configure/:path_to_inventory
        This method shows user a configuration panel
        """
        app = self.get_app( self.appname )
        inventory = find_inventory( app, url )            

        plb = self.project_lib_base

        # we want to save the original value so that "cancel" button works
        self._save_configuration_to_session( inventory )

        c = plb.c

        c.inventory = inventory
        c.url = url
        c.setButtonFactory = SetButtonFactory(self)
        c.traitLabelFactory = TraitLabelFactory(self)
        c.inputBoxFactory = InputBoxFactory(self)
        template = "pyregui/configure.myt"
        rt = self.render_response( template )
        return rt


    def main(self, appname):
        """handles :controller/:appname

        Shows the root page of a web application for the pyre application
        specified by 'appname'
        """
        plb = self.project_lib_base

        app = self.get_app( appname )
##         print session.__class__
##         print session
##         print id(session)
##         print session.__dict__
##         print dir(session)
##         print app

        session = plb.session
        session[ 'configuration' ] = {}
        session[ 'default_open_file' ] = open_default_inputfile
        session.save()
        
        c = plb.c
        c.appname = appname
        c.onelinehelp = onelinehelp( app )
        c.helpurl = helpurl( app )

        template = "pyregui/app.myt"
        return self.render_response( template )


    def save_configuration_start(self, url):
        """handle /:controller/:appname/save_configuration_start

        starting point of save configuration to a file
        """
        plb = self.project_lib_base

        controller_name = self.get_controller_name()
        appname = self.appname
        
        returnurl = '/'.join(
            ['', controller_name, appname, 'save_configuration' ] )
        
        session = plb.session
        session['returnurl'] = returnurl
        session.save()
        return plb.redirect_to( '/browser/writefile' )


    def save_configuration(self, url):
        """ handle /:controller/:appname/save_configuration

        save configuration to a pml file
        """
        plb = self.project_lib_base
        session = plb.session
        path = session['browser-pick']
        saveConfiguration( self.get_app( self.appname), path )
        return plb.redirect_to( todo = None )


    def run(self, url):
        """ handle /:controller/:appname/run

        run the pyre application
        """
        plb = self.project_lib_base
        appname = self.appname
        session = plb.session
        sid = id( session )
        import tempfile
        tmpdir = tempfile.mkdtemp( "%s-%s" % (appname, sid) )
        
        app = self.get_app( appname )
        pml = "%s.pml" % app.name

        saveConfiguration( app, os.path.join( tmpdir, pml ) )

        from pyreapp_registry import registry
        exe = registry.getExe( appname )

        launcher = self.get_app( "Launcher" )
        print launcher
        print launcher.__class__
        print launcher.__class__.__module__
        #os.system( "cd %s && %s && cd -" % (tmpdir, exe ) )
        curdir = os.path.abspath( os.curdir )
        os.chdir( tmpdir )
        launcher.main( exe )
        os.chdir( curdir )        

        try:
            # outputdir may be already set (see Propertysetter.py)
            outputdir = session['%s-outputdir'%appname]
        except:
            outputdir = tmpdir
        return plb.redirect_to( '/browser/browse/|%s' % outputdir )


    def get_app(self, appname):
        "retrieve application instance"
        from app_instances import get_app
        sid = id( self.project_lib_base.session)
        return get_app( appname, sid )


    def get_controller_name(self):
        "retrieve name of this controller"
        #this implementatoin is "hacky"
        return self.__class__.__module__.lower().split('.')[-1]


    def _restore_configuration_from_session(self, inventory):
        plb = self.project_lib_base
        configuration = plb.session['configuration']
        self._load_configuration( inventory, configuration )
        return


    def _save_configuration_to_session(self, inventory):
        "save configuration of an inventory to the session"
        plb = self.project_lib_base
        configuration = self._get_configuration( inventory )
        plb.session['configuration'].update( configuration )
        plb.session.save()
        return
    

    def _get_configuration(self, inventory):
        "get configuration of an inventory. return a dictionary"
        configuration = {}
        for trait in inventory.traits():
            name = trait.name()
            configuration[ '/'.join( [self.url or '',name] ) ] = trait.valueAsString()
            continue
        return configuration


    def _load_configuration(self, inventory, configuration ):
        "load configuration of an inventory from the given configuration store"
        plb = self.project_lib_base

        for trait in inventory.traits():
            name = trait.name()
            value = configuration[ '/'.join( [self.url or '',name] ) ]
            trait.setValue( value )
            continue

        return
    

    pass # end of MainController
        

def onelinehelp(app):
    try:
        onelinehelp = app.onelinehelp
    except:
        onelinehelp = getDocStr( app ).split('\n')[0][:40]
    return onelinehelp


def helpurl(app):
    try:
        helpurl = app.helpurl
    except:
        helpurl = 'http://danse.us'
    return helpurl


def getDocStr(app):
    candidate = app.__class__.__doc__
    if candidate is not None: return candidate
    else: return "Please consider writing a docstring for %s" % app.__class__
    raise



def find_property( app, path ):
    paths = path.split('/')
    inv = find_inventory(app, '/'.join( paths[:-1] ) )
    return inv.property( paths[-1] )



def find_inventory(app, path):
    print "find_inventory", path
    from pyregui.inventory.proxies.InventoryProxy import InventoryProxy
    appinvp = InventoryProxy( app.inventory )
    return _find_inventory( appinvp, path )



def _find_inventory( invp, path ):
    """get inventory proxy of a component inventory
    invp: proxy of an inventory
    path: path in the inventory that leads to the component

    Ex:
      invp:
        reducer
          normalizer
      _find_inventory( invp, 'reducer/normalizer' ) --> proxy( normalizer.inventory )
    """
    if path is None or len(path) == 0: return invp
    from pyregui.inventory.proxies.InventoryProxy import InventoryProxy
    paths = path.split( '/' )
    if len(paths) == 0: return invp
    name = paths[0]
    compinvp = InventoryProxy( invp.getComponentInventory( name ) )
    return _find_inventory( compinvp, '/'.join( paths[1:] ) )


def saveConfiguration( pyreapp, path = None ):
    "save configuration of pyreapp to the file given by path"
    from pyregui.inventory.configurationSaver import toPml
    name = pyreapp.name
    filename = "%s.pml" % name
    from os.path import join
    if path : filename = path
    toPml( pyreapp, filename )
    return



# version
__id__ = "$Id$"

# End of file 
