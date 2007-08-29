#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                   Jiao Lin
#                        California Institute of Technology
#                          (C) 2007  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
debug = journal.debug('wml.elements')

         

class Element:

    from AttributeDictionary import AttributeDictionary
    AttributeContainer = AttributeDictionary # overload this to use other container
    

    def __init__(self, attributes):
        attrs = self.AttributeContainer()
        for k,v in attributes.items():
            k = str(k)
            attrs.set(k, v)
        self.attributes = attrs
        self.children = []
        return


    def appendContent(self, content):
        debug.log("content=%s"%content)

        #pass empty string
        if len(content) == 0: return
        
        children = self.children

        children.append(content); return
        
        if len(children) == 0: children.append(content); return

        lastelem = children[-1]
        
        if isElement( lastelem ):
            #append the content string if the last child is an element
            children.append( content )
        elif isStr( lastelem ):
            #add ths content string to the pervious string
            children[-1] += ' ' + content
        else: raise ValueError, "don't know how to add %s" % content
        return


    def addChild(self, child):
        self.children.append( child )
        return


    def identify(self, visitor): raise NotImplementedError


    pass # end of Element


def isElement( candidate ): return isinstance( candidate, Element )

def isStr( candidate ): return isinstance(candidate, str ) or isinstance(candidate, unicode)
