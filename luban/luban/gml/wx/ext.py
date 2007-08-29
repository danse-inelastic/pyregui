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



# my extension to wx widgets, espeically event handling


from wx._core import EvtHandler



evthandlers = {}


def Bind(window, event, handler, source=None, id=-1, id2 = -1 ):
    evthandlers[ (window, event, source, id, id2) ] = handler
    EvtHandler.Bind(window, event, wrap_handler(handler), source, id, id2 )
    return


def wrap_handler( handler ):
    def h(wxevt):
        evt = Event( wxevt )
        return handler( evt )
    return h


def getEvtHandler(window, event, source=None, id=-1, id2=-1):
    return evthandlers.get( (window, event, source, id, id2) )


def bindCallbacks( window, events, callbacks, source=None, id=-1, id2=-1):
    """
    window: a wx window
    events: { event_name : wx event }
    callbacks: { event_name : callback }
    """
    for type, callback in callbacks.iteritems():
        if type.endswith('+'):
            todo = "append"
            type = type[:-1]
            pass
        elif type.startswith('+'):
            todo = "prepend"
            type = type[1:]
            pass
        else:
            todo = 'None'
        event = events[ type ]
        oldh = getEvtHandler( window, event )
        if oldh:
            if todo == "append":
                callback = combineHandlers( oldh, callback )
            elif todo == "prepend":
                callback = combineHandlers( callback, oldh )
            else:
                pass
            pass
        
        Bind(window, event, callback, source, id, id2)
        
        continue
    return


class Event(object):

    """ wrapper of wx event  to match event interface """


    def __init__(self, wxevt):
        object.__init__(self)
        self.wxevt = wxevt
        return


    def getKeyCode(self):
        return self.wxevt.GetKeyCode()


    def __getattribute__(self, name):
        if name in [
            'wxevt',
            'getKeyCode',
            ]: return object.__getattribute__(self, name)
        return getattr( self.wxevt, name )

    pass # end of Event
            

class Extension:

    def Bind(self, event, handler, source=None, id=-1, id2=-1):
        global Bind
        Bind(self, event, handler, source, id, id2)
        return


    pass # end of Extension


def combineHandlers( h1, h2 ):
    def h( evt ):
        h1(evt)
        h2(evt)
        return

    return h


# version
__id__ = "$Id$"

# End of file 
