#!/usr/bin/env python


import journal
debug = journal.debug("pyregui")


from utils import findExecutable

def getPyreApp( pathToExecutable, appClassName = None ):
    """return pyre application class given path to the app python file and
    optionally the class naem"""
    import os, sys

    path, appfilename = os.path.split(pathToExecutable)

    # should we add this if guard, or should we just
    # do a prepend no matter what.
    if not path in sys.path: 
        sys.path.insert(0, path)

    # splits the filename into file and extension, which are {py, pyc}
    basename, pyext = os.path.splitext(appfilename)
    m = __import__(basename)

    if appClassName: # if user supplies the class name, just use it
        App = m.__dict__.get(appClassName)
        if not App: raise RuntimeError, \
           "pyre application class %s cannot be found in %s" % (
            appClassName, pathToExecutable)
        return App
    
    App = None

    #find application classes
    Apps = []
    for key,item in m.__dict__.iteritems():

        # Looking for classes that subclasses Application
        try:
            debug.log ("test if %s is a pyre application" % item) 
            if issubclass(item, Application):
                Apps.append( item )
                pass
        except: 
            pass
        continue

    if not len(Apps): 
        raise "did not find any pyre application in %s" % appfilename

    Apps.sort( _younger )
    return Apps[0]



def runApp( App, executable, toolkit):
    debug.log( "start pyregui for pyre application %s" % App )
    from pyregui.WindowAppFactory import WindowAppFactory
    WindowApp = WindowAppFactory( App, executable, toolkit )
    try: windowApp = WindowApp()
    except Exception, msg:
        newmsg =  "Unable to start gui for application of class %s," % App.__name__
        newmsg += "because of %s, %s" % (msg.__class__, msg)
        print newmsg
        raise 
    windowApp.run()
    return


def run(appfilename, appClassName, toolkit):
    executable = findExecutable(appfilename)
    App = getPyreApp( executable, appClassName )
    runApp( App, executable, toolkit )
    return


def usage( appname ):
    return "Usage: %s path_to_pyre_application [pyre_application_class_name] " % ( appname, )


def mainTemplate( guitoolkit ):
    import sys
    if len(sys.argv) not in [2,3]:
       print usage(sys.argv[0])
       sys.exit(1)

    appfilename = sys.argv[1]
    appClassName = None
    if len(sys.argv) == 3: appClassName = sys.argv[2]

    import journal
    journal.error("pyre.inventory").deactivate()

    try:
        run( appfilename, appClassName, guitoolkit )
    except:
        raise
        print "%s failed" % ' '.join( sys.argv )
        print " - This might be due to an incorrect guess of the pyre application class."
        print " - Please specifiy the class name in the command line."
        print usage(sys.argv[0])
    return


from pyre.applications.Application import Application




def main():
    from pyregui.guitoolkit import wx
    mainTemplate( wx )
    return


if __name__ == "__main__": main()




#helpers
def _number_of_generations( subclass, base ):
    "number of generations between subclass and base"
    if not issubclass( subclass, base ):
        raise ValueError, "%s is not a subclass of %s" % (subclass, base)
    bases = subclass.__bases__
    if base in bases: return 1
    for b in bases:
        if issubclass( b, base ): return 1+_number_of_generations(b, base )
        continue
    raise RuntimeError, "should not reach here"


def _younger( cls1, cls2 ):
    "determine which pyre application is 'younger' relative to pyre application base class"
    return _number_of_generations( cls2, Application ) - _number_of_generations( cls1, Application )





# end of file
