#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.applications.Script import Script


class TrivialApp(Script):

    "A trivial pyre application that prints out greetings"

    class Inventory(Script.Inventory):

        import pyre.inventory

        name = pyre.inventory.str('name', default='world')
        name.meta['tip'] = 'the entity to greet'

        greeter = pyre.inventory.facility('greeter', default = 'hello')


    def main(self, *args, **kwds):
        print 'Hello %s!' % self.friend
        self.greeter.greet( self.friend )
        return


    def __init__(self):
        Script.__init__(self, 'trivial')
        self.friend = ''
        return


    def _defaults(self):
        Script._defaults(self)
        return


    def _configure(self):
        Script._configure(self)
        self.friend = self.inventory.name
        self.greeter = self.inventory.greeter
        return


    def _init(self):
        Script._init(self)
        return



def main():
    app = TrivialApp()
    return app.run()


# main
if __name__ == '__main__':
    # invoke the application shell
    main()


# version
__id__ = "$Id$"


# End of file 
