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


def run(toolkit, maingml):
    from luban.gml import toolkits
    toolkit = toolkits.__dict__[ toolkit]
    if toolkit is None: raise "Cannot find toolkit %s" % toolkit
        
    from controllers.MainController import MainController
    m = MainController ( toolkit, maingml )
    m.main()
    return


def main():
    run( 'wx', 'main.gml' )



if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
