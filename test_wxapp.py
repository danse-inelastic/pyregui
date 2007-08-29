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
unittests for wxapp. This should be run from the source directory
because some of the tests assume the relative existence of certain files.

may be already defunct, since wxapp.py is gone
"""

import unittest, os
from wxapp import *

from pyre.components.Component import Component


class TestWxapp(unittest.TestCase):

    def test_findExecutable(self):
        # wxapp.py should be in this directory
        exe = findExecutable("wxapp.py")
        self.assert_(exe == "wxapp.py")

    def test_findPython(self):
        exe = findExecutable("python")
        self.assert_(os.path.exists(exe))

    def test_findSudoku(self):
        exe = findExecutable("../sudoku_solver.py")
        self.assert_(os.path.exists(exe))

    def test_getPyreApp(self):
        from pyre.applications.Application import Application
        exe = findExecutable("../sudoku_solver.py")
        app = getPyreApp(exe)
        self.assert_(issubclass(app, Application))

     

if __name__=='__main__':
    unittest.main()


# version
__id__ = "$Id: test_wxapp.py,v 1.2 2006/08/10 23:37:36 patrickh Exp $"

# End of file
