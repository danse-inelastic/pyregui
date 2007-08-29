#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component


class hello(Component):

    'A greeter that says "hello"'

    class Inventory(Component.Inventory):

        import pyre.inventory
        greeting = pyre.inventory.str( 'greeting', default = 'hello' )
        pass


    def greet(self, name):
        greeting = self.greeting
        print "%s %s" % (greeting, name)
        return


    def __init__(self, name, facility = "greeter"):
        Component.__init__(self, name, facility=facility)
        return


    def _defaults(self):
        Component._defaults(self)
        return


    def _configure(self):
        Component._configure(self)
        self.greeting = self.inventory.greeting
        return


    def _init(self):
        Component._init(self)
        return


def greeter(): return hello( 'hello' )

# version
__id__ = "$Id$"

# End of file 
