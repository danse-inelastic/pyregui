#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## \package pyregui.ppyreapp_ext
## This package contains classes that extends pyre Application
## class a little bit (actually only the "run" method).
## The original run method is a lengthy one with many steps
## of operations.
## Here we break down the run method to smaller pieces so that
## it is easier to customize it.


class PyreApp_ExtRunMethod:

    #break the pyre Application "run" method into pieces.
    #some implementation details are
    #copied from pyre.applications.Application


    def run(self, *args, **kwds):
        #this method group codes in the original pyre.Application.run method
        #to some methods. Now we can customize the run method to
        #do things we want.
        self.run_collectConfiguration()
        self.run_applyConfiguration()
        self.init()
        self.run_runWithConfiguration()
        self.fini()
        return


    def run_collectConfiguration(self):
        registry = self.createRegistry()
        self.registry = registry

        self.requestedForHelp, self.argv = self.processCommandline(registry)

        curator = self.createCurator()
        self.initializeCurator(curator, registry)

        self.initializeConfiguration()

        self.collectUserInput(registry)

        self.updateConfiguration(registry)
        return


    def run_applyConfiguration(self):
        self.unknownProperties, self.unknownComponents = self.applyConfiguration()
        return
    
        
    def run_runWithConfigurations(self, *args, **kwds):
        self.generateBanner()

        if self.requestedForHelp:
            self.help()
        elif self._showHelpOnly:
            pass
        elif self.verifyConfiguration(self.unknownProperties, self.unknownComponents,
                                      self.inventory.typos):
            self.execute(*args, **kwds)
        return


    pass # end of  PyreApp_ExtRunMethod



# $Id: WindowAppFactory.py,v 1.1 2006/08/09 23:09:22 linjiao Exp $

# end of file
