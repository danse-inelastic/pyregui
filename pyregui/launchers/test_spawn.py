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
unittests for spawn
"""

from test import test_support
import unittest
from spawn import *

class TestSpawn(unittest.TestCase):

    def test_which(self):
        cmd = "which mpipython.exe"
        self.assert_(spawn(cmd)==0)

    def test_ls(self):
        cmd = "date > /dev/null"
        self.assert_(spawn(cmd)==0)

    def test_ls2(self):
        cmd = ["ls", "-alt"]
        self.assert_(spawn(cmd)==0)


     

def test_main():
    test_support.run_unittest(TestSpawn)
    
if __name__=='__main__':
    test_main()


# version
__id__ = "$Id: test_spawn.py,v 1.1 2006/08/10 02:06:32 patrickh Exp $"

# End of file
