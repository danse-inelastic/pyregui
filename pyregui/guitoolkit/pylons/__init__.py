#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                   (C) Copyright 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



## pyregui toolkit for pylons project
## To make it usable, make a new controller which need to be
## inherited from MainController
##
## 1. make a symbolic link to the templates in the "resources" directory
##    in the pylons project's templates directory
##
## 2. To make this work, we also need a browser controller.
##
## 3. routing must be changed accordingly
##
##    map.connect('pyreapp/:appname/:todo/*url', controller='pyreapp', appname=None, todo=None, url='')
##    map.connect('browser/:purpose/*url', controller='browser', purpose='readfile', url=None)
##
## Examples of how to use this toolkit is in directory "example"


__depends__ = [
    'pylons',
    'pyre',
    ]


# version
__id__ = "$Id:  2006-09-13 07:00:52Z linjiao $"

# End of file 
