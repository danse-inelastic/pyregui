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
# This visitor handles the action after the control comes back from
# the "dialog" activated by the button. For the "browse" example,
# this is after the browser "dialog" has not finished and returned
# the user-selected file path in "session".


class PropertySetter:

    """set a property to a new value"""


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
        session = plb.session

        path = session['browser-pick']
        inputfile.setValue( path )

        #back up one level to inventory
        url =  '/'.join( parent.url.split( '/' )[:-1] )
        return plb.redirect_to( todo="configure", url=url )
    methods[ 'inputfile' ] = oninputfile


    def onoutputdir( self, outputdir ):
        parent = self.parent
        plb = parent.project_lib_base
        session = plb.session

        path = session['browser-pick']
        outputdir.setValue( path )

        appname = parent.appname
        session['%s-outputdir' % appname ] = path
        session.save()

        #back up one level to inventory
        url =  '/'.join( parent.url.split( '/' )[:-1] )
        return plb.redirect_to( todo="configure", url=url )
    methods[ 'outputdir' ] = onoutputdir

    pass # end of PropertySetter


# version
__id__ = "$Id$"

# End of file 
