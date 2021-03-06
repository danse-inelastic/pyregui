#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def run(toolkit, gmls):
    from luban.gml import toolkits
    toolkit = toolkits.__dict__[ toolkit]
    if toolkit is None: raise "Cannot find toolkit %s" % toolkit
        
    from controllers.MainController import MainController
    m = MainController ( toolkit, gmls )
    m.main()
    return


def main():
    import os
    curdir = os.path.abspath( '.' )
    import sys
    sys.path = [curdir] + sys.path
    
    import journal
    journal.debug( 'gml-wx-renderer' ).activate()
    run( 'wx',  ['main.gml', 'hello.gml' ] )
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
