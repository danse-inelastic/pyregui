#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                         (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component
class Optimizer( Component ): pass


from pyre.applications.Script import Script as Base


class SimpleApp(Base):


    class Inventory(Base.Inventory):

        import pyre.inventory

        name = pyre.inventory.str('name', default='world')
        name.meta['tip'] = 'the entity to greet'

        optimizer = pyre.inventory.facility('optimizer', default=Optimizer('optimizer', 'optimizer' ) )
        optimizer.meta['tip'] = 'The optimizer'

        parameter1 = pyre.inventory.float('parameter1', default=0.0)
        parameter1.meta['tip'] = 'The parameter # 1'

        parameter2 = pyre.inventory.float('parameter2', default=0.0)
        parameter2.meta['tip'] = 'The parameter # 2'

        parameter3 = pyre.inventory.float('parameter3', default=0.0)
        parameter3.meta['tip'] = 'The parameter # 3'

        parameter4 = pyre.inventory.float('parameter4', default=0.0)
        parameter4.meta['tip'] = 'The parameter # 4'

        parameter5 = pyre.inventory.float('parameter5', default=0.0)
        parameter5.meta['tip'] = 'The parameter # 5'

        parameter6 = pyre.inventory.float('parameter6', default=0.0)
        parameter6.meta['tip'] = 'The parameter # 6'

        parameter7 = pyre.inventory.float('parameter7', default=0.0)
        parameter7.meta['tip'] = 'The parameter # 7'
        parameter7.meta['opacity'] = 10

        parameter8 = pyre.inventory.float('parameter8', default=0.0)
        parameter8.meta['tip'] = 'The parameter # 8'
        parameter8.meta['opacity'] = 10

        parameter9 = pyre.inventory.float('parameter9', default=0.0)
        parameter9.meta['tip'] = 'The parameter # 9'
        parameter9.meta['opacity'] = 10

        parameter10 = pyre.inventory.float('parameter10', default=0.0)
        parameter10.meta['tip'] = 'The parameter # 10'
        parameter10.meta['opacity'] = 10

        parameter11 = pyre.inventory.float('parameter11', default=0.0)
        parameter11.meta['tip'] = 'The parameter # 11'
        parameter11.meta['opacity'] = 100

        parameter12 = pyre.inventory.float('parameter12', default=0.0)
        parameter12.meta['tip'] = 'The parameter # 12'
        parameter12.meta['opacity'] = 1000

        from MolDynamics import MolDynamics
        molDynamics = pyre.inventory.facility('molecular_dynamics_engine', default = MolDynamics('MolDynamics') )
        molDynamics.meta['known_plugins'] = ['gulp']
        pass # end of inventory


    def main(self, *args, **kwds):
        print 'Hello %s!' % self.friend
        return


    def __init__(self):
        Base.__init__(self, 'simple')
        self.friend = ''
        return


    def _configure(self):
        Base._configure(self)
        self.friend = self.inventory.name
        return

    pass # end of SimpleApp


def main():
    # invoke the application shell
    app = SimpleApp()
    return app.run()


# main
if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Tue Oct  3 20:08:36 2006

# End of file 
