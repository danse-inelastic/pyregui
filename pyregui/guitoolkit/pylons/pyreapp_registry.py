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


# registry of pyre applications


class Registry:

    def __init__(self):
        self._store = {}
        self._seq = []
        return


    def register(self, appName, exe, className ):
        from pyregui.pyreui import getPyreApp, findExecutable
        pathToExecutable = findExecutable( exe )
        App = getPyreApp( pathToExecutable, className )
        self._store[ appName ] = {
            'Class': App,
            'exe': pathToExecutable,
            }
        self._seq.append( appName )
        return


    def getApp(self, appname):
        return self._store[ appname ]['Class']


    def getExe(self, appname):
        return self._store[ appname ]['exe']


    #def __iter__(self): return self._store.__iter__()
    def __iter__(self): return self._seq.__iter__()


    pass # end of Registry



registry = Registry()

        
# version
__id__ = "$Id$"

# End of file 
