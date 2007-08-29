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


from template import parse as parse_template

from Parser import Parser
default_parser = Parser()


def parse( stream ): return default_parser.parse( parse_template(stream) )

def parse_file( filename ): return parse( open( filename ) )



from WxRenderer import Renderer as WxRenderer
default_wxrenderer = WxRenderer()


def render_gui( guitree, controller, guirenderer ):
    from Options import Options
    options = Options('weaver')
    guirenderer.options = options
    return guirenderer.render( guitree, controller )


def gml2gui( gmlfile, controller, guirenderer ):
    return render_gui( parse_file( gmlfile ), controller, guirenderer )
    


#----------------------------------------------------------------------
# extend gml to a new gui element
#  elements: add a new class
#  parser: add a new class
#  wx: add a new class. add a factory method in __init__
#  WxRenderer: add a new handler
#


#----------------------------------------------------------------------
#wx specific. only for testing purpose.
def render_wxgui(guitree, controller):
    return render_gui( guitree, controller, default_wxrenderer )


def gml2wxgui( filename, controller ):
    return gml2gui( filename, controller, default_wxrenderer )


__all__ = [ default_parser, parse, parse_file, render_wxgui, gml2wxgui ]


import journal
#journal.debug('wml.elements').activate()
#journal.debug("html-renderer").activate()

# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
