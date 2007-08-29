#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                         (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# this module has not been good enough to anything useful
# it cannot deal with any gui elements like frame, panel, etc

from pyre.weaver.mills.XMLMill import XMLMill

import journal
debug = journal.debug("html-renderer")

class Renderer(XMLMill):


    def render(self, gui, controller):
        self._cur_sec_level = 0
        self.controller = controller
        return gui.identify(self)


    def registerDecorator(self, decorator, *args):
        _register( args, decorator, self._decorators )
        return


    # handlers

    def onGui(self, gui):
        self.expand( gui )
        return

    
    def expand(self, element):
        for child in element.children:
            if isElement(child): child.identify(self)
            elif isStr(child):
                self._write( child )
            else: raise ValueError
            continue
        return


    def onSection(self, section):
        self._indent()
        self._write('')
        decorator = self._decorators['section']
        
        self._write(decorator.start())

        self._indent()

        label = section.attributes.get('label')
        if label:
            self._write( '<a name="%s"></a>' % label )
            pass
        title = section.attributes['title']
        title_decorator = self._decorators[ "title" ][ 'section%d' % self._cur_sec_level ]
        start,end = title_decorator.decorations()
        self._write('%s %s %s' % (start, title, end) )

        self._cur_sec_level += 1
        self.expand( section )
        self._cur_sec_level -= 1

        self._outdent()

        self._write(decorator.end())
        self._write('')
        self._outdent()
        return


    def onParagraph(self, paragraph):
        self.onElement( paragraph )
        return


    def onNote(self, note):
        self.onElementWithTitle( note )
        return


    def onLink(self, link):
        address = link.attributes['address']
        self._write('')
        self._write('<a href="%s">'%address)
        self.expand( link )
        self._write('</a>')
        self._write('')
        return


    def onTable(self, table):
        #this implementation wraps a table in a note page
        #not the best way to do things. but it works for now
        #TODO, make a better one so templating is easier
        note_decorator = self._decorators[ 'note' ]
        title_decorator = self._decorators[ 'title' ]['note']
        decorator = self._decorators['table']
        title = table.attributes['title']
        self._write('')
        self._write( note_decorator.start() )
        self._write( title_decorator.decorate( title ) )
        self._write( decorator.start() )
        self._indent()
        self.expand(table)
        self._outdent()
        self._write( decorator.end() )
        self._write( note_decorator.end() )
        self._write('')
        return
    

    def onRow(self, row):
        self.onElement( row )
        return
    

    def onCell(self, cell):
        self.onElement( cell )
        return


    def onEmphasis(self, e):
        self.onElement( e )
        return


    def onList(self, l):
        self.onElement( l )
        return


    def onListItem(self, li):
        self.onElement( li )
        return


    def onCode(self, code):
        self._write('')
        self._write('<div class="syntax"><table>')
        self._indent()
        for i,l in enumerate(code.children):
            self._write('<tr>')
            self._indent()
            self._write('<td class="linenos"><pre>%d</pre></td>' % (i+1) )
            self._write('<td class="code"><pre>%s</pre></td>' % l)
            self._outdent()
            self._write('</tr>')
            continue
        self._outdent()
        self._write('</table></div>')
        return


    def onFigure(self, figure):
        #this implementation wraps a table in a note page
        #not the best way to do things. but it works for now
        #TODO, make a better one so templating is easier
        note_decorator = self._decorators[ 'note' ]
        title_decorator = self._decorators[ 'title' ]['note']

        file = figure.attributes['file']
        width = figure.attributes.get('width')
        title = figure.attributes['title']
        
        self._write( '' )
        self._write( note_decorator.start() )
        self._write( title_decorator.decorate( title ) )
        self._write( '<table border=0 align="center"><tr><td>' )
        self._write( '<div class="plain">' )
        self._write( '<img src="%s" width=%s>' % (file, width) )
        self._write( '</div>' )
        self._write( '</td></tr></table>' )
        self._write( note_decorator.end() )
        self._write( '' )
        return


    def onElement(self, element):
        decorator = self._decorators[ _typestr(element ) ]
        self._write('')
        self._write( decorator.start() )
        self._indent()
        self.expand(element)
        self._outdent()
        self._write( decorator.end() )
        self._write('')
        return
    

    def onElementWithTitle(self, element):
        title = element.attributes['title']
        type = _typestr(element)
        decorator = self._decorators[ type ]
        title_decorator = self._decorators[ 'title' ][type]
        self._write('')
        self._write(decorator.start())
        self._write( title_decorator.decorate( title ) )
        self.expand( element )
        self._write(decorator.end())
        self._write('')
        return


    def __init__(self):
        XMLMill.__init__(self)
        self.firstLine = "" # originally <?xml version=1.0>
        from html import default_decorators
        self._decorators = default_decorators
        return


    def _renderDocument(self, document):
        return document.identify(self)


    pass # end of Renderer



#helper functions

from arcs.wml.elements.Element import isStr, isElement


def _typestr( element ):
    return element.__class__.__name__.lower()

def _register( keys, value, registry):
    #recursively reigister a value with multiple keys to registry
    key = keys[0]
    if len(keys)==1: registry[key] = value
    t = registry.get(key)
    if t is None: registry[key] = {}
    _register( keys[1:], value, registry[key] )


# version
__id__ = "$Id: Renderer.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
