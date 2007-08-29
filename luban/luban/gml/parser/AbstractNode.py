#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
debug = journal.debug("gml.parser")


from pyre.xml.Node import Node
import urllib


class AbstractNode(Node):

    ElementFactory = None # overload this to provide factory method of creating element

    def __init__(self, document, attributes):
        Node.__init__(self, document)

        self.element = self.ElementFactory(attributes)
        return


    def notify(self, parent):
        return self.element.identify( parent )


    def content(self, content):
        debug.log( "content=%s" % content )
        content = content.strip()
        if len(content)==0: return
        self.element.appendContent( urllib.unquote(content).strip() )
        self.locator = self.document.locator
        return


    def onElement(self, element):
        self.element.addChild( element )
        return

    pass


# version
__id__ = "$Id: AbstractNode.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
