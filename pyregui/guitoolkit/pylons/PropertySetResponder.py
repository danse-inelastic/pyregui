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


# property usually does not have a "set" button. but sometimes it could be useful.
# for example, when we are dealing with a property that is the path to an
# input data file, it would be nice to have a browse button.
# This visitor responds to the event of user pressing the "set"
# button next to a property.
# For the "browse" example,
# this visitor creates a browser form when the "browse" button is pressed.


class PropertySetResponder:

    """respond to a set-button event for a property"""


    def __init__(self, parent):
        self.parent = parent
        return


    def __call__(self, property):
        return self.dispatch( property ) ( self, property )


    def dispatch(self, property):
        return self.methods[ property.type() ]


    methods = {}


    def oninputfile( self, inputfile ):
        parent = self.parent
        plb = parent.project_lib_base
        appname = parent.appname
        url = parent.url or ''
        controller_name = parent.get_controller_name()

        propname = inputfile.name()
        # when return from browser, redirect to method in PropertySetter
        returnurl = '/'.join( ['', controller_name, appname, 'setProperty', url, propname ] )
        
        session = plb.session
        session['returnurl'] = returnurl
        session.save()
        print returnurl

        return plb.redirect_to( "/browser/readfile" )
    methods[ 'inputfile' ] = oninputfile


    def onoutputdir( self, outputdir ):
        parent = self.parent
        plb = parent.project_lib_base
        appname = parent.appname
        url = parent.url or ''
        controller_name = parent.get_controller_name()

        propname = outputdir.name()
        # when return from browser, redirect to method in PropertySetter
        returnurl = '/'.join( ['', controller_name, appname, 'setProperty', url, propname ] )
        
        session = plb.session
        session['returnurl'] = returnurl
        session.save()
        print returnurl

        return plb.redirect_to( "/browser/outputdir" )
    methods[ 'outputdir' ] = onoutputdir


    pass # end of PropertySetResponder


# version
__id__ = "$Id$"

# End of file 
