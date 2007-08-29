# this is an example on how to use this toolkit in a pylons project

from arcs.lib.base import *

from pyregui.guitoolkit.pylons.MainController import MainController


import register_pyre_apps



class PyreappController(MainController, BaseController):

    import arcs.lib.base as project_lib_base

    def __init__(self, *args, **kwds):
        MainController.__init__(self)
        BaseController.__init__(self, *args, **kwds)
        return
    

    pass # end of PyreappController


