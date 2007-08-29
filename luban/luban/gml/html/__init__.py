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


def decorator( *args, **kwds ):
    from Decorator import Decorator
    return Decorator( *args, **kwds )

d = decorator

default_decorators = {
    "title": {"section0": d( 'h1', {"class":"pudge-member-page-heading"} ),
              "section1": d( 'h1' ),
              "section2": d( 'h2' ),
              "section3": d( 'h3' ),
              "section4": d( 'h4' ),
              "note": d( 'p', {"class":"first admonition-title"} ),
              },
    "section":    d("div"),
    "note":       d("div", {"class": "note"} ),
    "paragraph":  d('p'),
    "table":      d('table', {'width':"80%", 'border':"1",'cellspacing':"1", "align":'center'} ),
    'row':        d('tr'),
    'cell':       d('td'),
    'emphasis':   d('b'),
    'list':       d('ul'),
    'listitem':   d('li'),
    }


__all__ = [ decorator, default_decorators ]

# version
__id__ = "$Id: Paragraph.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
