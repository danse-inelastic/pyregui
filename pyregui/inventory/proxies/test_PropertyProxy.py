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
unittests for PropertyProxy
"""

import unittest
from PropertyProxy import *

from pyre.components.Component import Component

class Inventory(Component.Inventory):
    import pyre.inventory as inv
    a = inv.str('a', default =  'abc' )
    a.meta['known_alternatives'] = ['def','ghi']
    b = inv.float('b', default = 3.0 )

class TestPropertyProxy(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory("i")
        self.ap = PropertyProxy(self.inventory, Inventory.a)

    def test_name(self):
        self.assert_(self.ap.name() == "a")

    def test_value(self):
        self.assert_(self.ap.value() == "abc")

    def test_type(self):
        self.assert_(self.ap.type() == "str")

    def test_alternatives(self):
        self.assert_('def' in self.ap.known_alternatives())
        self.assert_('ghi' in self.ap.known_alternatives())
        self.assert_('xxx' not in self.ap.known_alternatives())

    def test_setvalue(self):
        self.ap.setValue("def")
        self.assert_(self.ap.value() == "def")
        # need to unset to make sure that the test results do not depend on 
        # order
        self.ap.setValue("abc")

    def test_pp(self):
        bp = PropertyProxy(self.inventory, Inventory.b)
        self.failUnlessRaises(ValueError, bp.setValue, 'a')
        
     

if __name__=='__main__':
    unittest.main()


# version
__id__ = "$Id: test_PropertyProxy.py,v 1.2 2006/08/04 22:43:09 patrickh Exp $"

# End of file
