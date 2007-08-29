#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Patrick Hung, Caltech
#                        (C) 1998-2006  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
unittests for TraitProxy
"""

import unittest
from TraitProxy import *

from pyre.components.Component import Component

class Inventory(Component.Inventory):
    import pyre.inventory as inv
    a = inv.str('a', default =  'abc' )
    a.meta['tip'] = "a is the first alphabet"

class TestTraitProxy(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory("i")
        self.ap = TraitProxy(self.inventory, Inventory.a)

    def test_name(self):
        self.assert_(self.ap.name() == "a")

    def test_value(self):
        self.assert_(self.ap.value() == "abc")

    def test_type(self):
        self.assert_(self.ap.type() == "str")

    def test_tip(self):
        self.assert_(self.ap.tip() == Inventory.a.meta['tip'])

    def test_setvalue(self):
        self.ap.setValue("def")
        self.assert_(self.ap.value() == "def")
        # need to unset to make sure that the test results do not depend on 
        # order
        self.ap.setValue("abc")

     

if __name__=='__main__':
    unittest.main()


# version
__id__ = "$Id: test_TraitProxy.py,v 1.1 2006/08/04 22:30:14 patrickh Exp $"

# End of file
