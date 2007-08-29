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


## Store of pyre application instances
## This module temporarily solve the problem of save pyre application instance
## with session. Currently we cannot save pyre app instance directly to a
## session due to pickle problem. We should solve that and ensure every pyre
## app is picklable.


class AppInstances:

    """Store of instances.

    The main interface is method "get".
    """

    def __init__(self, appFactory, limit = 5):
        """create store.

        appFactory: factory method to create an app instance from given signature
        limit: size limit of this store
        """
        self._store = {}
        self._sequence = []
        self._factory = appFactory
        self._limit = limit
        return


    def size(self): return len(self._store)


    def get(self, signature):
        """return an instance given signature

        if it is found already in the store, a reference to the instance
        in the store will be returned.
        otherwise, a new instance will be created and saved in the store.
        """
        if self.size() > self._limit:
            self.reduce_to_limit( )
            pass

        store = self._store
        
        app = store.get ( signature )
        if app: return app

        app = self._create_app( signature )

        self._add( signature, app )

        return app


    def reduce_to_limit(self):
        """reduce size of the store

        The store cannot be expanding forever. We need to reduce the
        size of this store whenever it is over limit.
        """
        n = self.size() - self._limit 
        for i in range(n):
            self._delete( self._sequence[ i ] )
            continue
        return

                
    def _delete(self, signature):
        del self._store[signature]
        del self._sequence[ self._sequence.index( signature ) ]
        return
    

    def _add(self, signature, app):
        self._store[signature] = app
        self._sequence.append( signature )
        return
    

    def _create_app( self, appname ):
        return self._factory(appname)

    pass # end of AppInstances

        
        

def create_app( signature ):
    appname, sid = signature
    
    from pyreapp_registry import registry
    App = registry.getApp( appname )
        
    app = AppFactory(App) ()
    app.prerun()
    
    return app

    
app_instances = AppInstances(create_app, limit=100)


def get_app(appname, session_id):
        
    signature = appname, session_id
    
    return app_instances.get( signature )
        

from pyregui.WindowAppFactory import NewRun_for_PyreApp


def AppFactory(PyreAppClass):
    
    class WindowApp( PyreAppClass, NewRun_for_PyreApp ):

        __doc__ = PyreAppClass.__doc__
        
        
        def __init__(self):
            PyreAppClass.__init__(self)
            return
        
        
        def prerun(self, *args, **kwds): return NewRun_for_PyreApp.run(self, *args, **kwds)


        def run(self, *args, **kwds):
            print "%s" % PyreAppClass.run
            return PyreAppClass.run(self, *args, **kwds)

        
        def collectConfigurationsFromGui(self): return

        pass # end of WindowApp
        
    return WindowApp


def test():
    def f(s):
        f.counter += 1
        return f.counter
    f.counter = 0
    limit = 5
    instances = AppInstances( f, limit )

    assert instances.get( None ) == 1
    assert instances.get( 1 ) == 2
    assert instances.get( 1 ) == 2
    assert instances.get( 0 ) == 3
    assert instances.get( 10 ) == 4
    assert instances.get( 3 ) == 5
    assert instances.get( 'a' ) == 6
    assert instances.size() == limit + 1
    assert instances.get( 'b' ) == 7
    assert instances.size() == limit + 1
    assert instances.get( 1 ) == 8
    return


if __name__ == "__main__": test()

# version
__id__ = "$Id$"

# End of file 
