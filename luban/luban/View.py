#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class View(object):

    def __init__(self):
        self._store = {}
        return


    def getSubview(self, name):
        return self._store.get(name)


    def setSubview(self, name, subview):
        self._store[name] = subview
        return



# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
