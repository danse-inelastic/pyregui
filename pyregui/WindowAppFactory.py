#!/usr/bin/env python


class WindowPyreMixin(object):


    def __init__(self, pyreapp_executable, toolkit):
        self.pyreapp_executable  = pyreapp_executable
        self.toolkit = toolkit
        return


    def enterWindowEventLoop(self):
        MainWindowApp = self.toolkit.MainWindowApp
        #print "in %s" % self.__class__.__name__
        mainWin = MainWindowApp(self, self.pyreapp_executable, self.toolkit)
        mainWin.MainLoop()
        return 

    # end of Class WindowPyreMixin



from pyreapp_ext import PyreApp_ExtRunMethod
class NewRun_for_PyreApp(PyreApp_ExtRunMethod):


    def run(self, *args, **kwds):
        self.run_collectConfiguration()
        self.run_applyConfiguration()
        self.collectConfigurationsFromGui()
        return


    def collectConfigurationsFromGui(self):
        raise NotImplementedError, "%s must define collectConfigurationsFromGui" % \
              self.__class__.__name__


    pass # end of NewRun_for_PyreApp



def WindowAppFactory(PyreAppClass, pyreapp_executable, toolkit):
   class WindowApp( PyreAppClass, WindowPyreMixin, NewRun_for_PyreApp ):

       __doc__ = PyreAppClass.__doc__


       def __init__(self):
           PyreAppClass.__init__(self)
           WindowPyreMixin.__init__(self, pyreapp_executable, toolkit)
           return


       def run(self): return NewRun_for_PyreApp.run(self)


       def collectConfigurationsFromGui(self):
           self.enterWindowEventLoop()
           return

       # end of WindowApp


   return WindowApp

# $Id: WindowAppFactory.py,v 1.1 2006/08/09 23:09:22 linjiao Exp $

# end of file
