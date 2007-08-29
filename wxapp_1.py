#!/usr/bin/env python
#

from pyregui.WxAppFactory import wxAppFactory
from pyregui.introspect import import_app, get_pyre_Apps


def main():
    import sys
    if len(sys.argv) != 2:
       print "Usage: %s path_to_pyre_application" % __file__
       sys.exit(1)

    import os
    path, appfilename = os.path.split(sys.argv[1])
    executable = sys.argv[1]

    sys.path.append(path)
    
    mod = import_app(sys.argv[1])
    App = get_pyre_Apps(mod)[0]

    WxApp = wxAppFactory( App, executable )
    wxApp = WxApp()
    wxApp.run()
    return


if __name__ == "__main__": 
    main()

# $Id: wxapp_1.py,v 1.2 2006/08/05 08:22:46 patrickh Exp $
# end of file
