#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Patrick Hung, Caltech
#                        (C) 1998-2006  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
Introspection for pyre.
"""

import inspect
from pyre.inventory.Property import Property
from pyre.inventory.Facility import Facility
from pyre.components.Component import Component

def visibleitem(name, visible_list=None):
    """
Decides which inventory items are to be listed.

some segments from pydoc.visiblename.
    """
    # Certain special names are redundant.
    specials = ('__builtins__', '__doc__', '__file__', '__path__',
                '__module__', '__name__', '__slots__')
    defaults = ('showComponents', 'showCurator', 'showProperties', 'usage', 'journal', 'weaver')
    if name in specials+defaults:
        return 0
    # Private names are hidden, but special names are displayed.
    if name.startswith('__') and name.endswith('__'): return 1
    if visible_list is not None:
        # only document that which the programmer exported in visible_list
        return name in visible_list
    else:
        return not name.startswith('_')


def normalize_plugin_name(str, facility_name):
    # if name is already dot-separated, check whether the last piece of the string is the facility name
    if str.find('.') > 0 and str.split('.')[-1] == facility_name:
        return str
    else:
        return '.'.join([str, facility_name])

def import_plugin(strname):
    """
Importing a 'plugin' by name.
e.g., if we are trying to do
from nintegrate.transcendental.sin import func
the import statement will read mod =  __import__('nintegrate.transcendetal.sin')
and we will need to retrieve transcendental.sin from mod. (we need to do a Nest).

Usually a call to this is preceded by a normalize_plugin_name. 
e.g., if there is a facility called "func" and the component is to be created by
from nintegrate.transcendentals.log import func, then normalize_plugin_name will
append the name of the facility "func" to the module.

Special case. If nintegrate.transcendentals.log has factory name function, and not 
the default 'func', then the string "nintegrate.transcendentals.log.function" should be
passed in. (it will get normalized to have a .func suffix, but the last if/else clause
will catch it)
    """

    try:
        t = strname.split('.')
        print t
        mod =  __import__('.'.join(t[0:-1]))    

        for name in t[1:-1]:
            mod = getattr(mod, name)

        if hasattr(mod, t[-1]):
             plugin = getattr(mod, t[-1])
        else:
             plugin = mod

        #return plugin()
        if callable(plugin):
             return plugin()
        else:
            return getattr(plugin, t[-1])()

    except:
        print "Failed to import %s from %s" % (t[-1], '.'.join(t[0:-1]))
        raise


def get_plugin(plugin_name, facility_name):
    """
 Given a facility called visualizer, and a component called matlab_board (for example)....
 then get_plugin('matlab_board', 'visualizer') will do the equiv 
 of from matlab_board import visualizer. The output can be passed into introspect.
    """
    
    return import_plugin(normalize_plugin_name( plugin_name, facility_name )) 

def display_inventory_attribute(inventory, attr):
    """
 inventory should be an instance of pyre Inventory.
 attr should be a tuple from the output of inspect.classify_class_attrs
    """
    attrname = attr[0]
    thisprop = inventory.__dict__[attrname]
    if thisprop.meta.has_key('tip'):
        tip = ' --- [Tip: %s] ' % thisprop.meta['tip']
    else:
        tip = ''
    return attrname + tip
   
def get_by_name(cls, name):
    if name in cls.__dict__:
        return cls.__dict__[name]
    else:
        return getattr(cls, name)

def retrieve_plugin(pyreapp, facility, plugin):
    """
Retrieves and instantiates pyre component by name.
e.g., retrieve_plugin(app, 'func', 'sin')
    """
    p = pyreapp.inventory._traitRegistry[facility]
    if plugin.startswith('<<Factory>>'):
        inst = p.factory()
    else:
        inst, locator = p._retrieveComponent(pyreapp.inventory, plugin)
    return inst

  
def introspect(pyreapp):
    # introspecting into the Inventory of a pyre app or a pyre component
    rootobj = pyreapp
    inventory = pyreapp.Inventory

    # find attributes of inventory
    attrs = inspect.classify_class_attrs(inventory)
    attrs = filter(lambda (name, kind, cls, value): visibleitem(name), attrs)

    # from the mro, find type of self
    mro = inspect.getmro(inventory)
    if mro:
        thisclass = mro[0]
    else:
        thisclass = attrs[0][2]

    # filter and not show any inventories that are inherited
    myattrs = filter(lambda (name, kind, cls, value): cls == thisclass, attrs)

    # want to actually do this (but they are not compatible with how I am doing things)
    myattrs = filter(lambda (name, kind, cls, value): not name.startswith('__'), attrs)

    properties = filter(lambda (name, kind, cls, value): issubclass(type(value), Property), myattrs)
    facilities = filter(lambda (name, kind, cls, value): issubclass(type(value), Facility), myattrs)
    # other classes which are not a descendent of Facility, but nonetheless have Inventory
    #others = filter(lambda (name, kind, cls, value): hasattr(value, 'Inventory') , myattrs)

    children = []

    # Do the properties first
    for i,x in enumerate(properties):
       thisproperty = x[3]
       children.append(thisproperty)

    # now the pyre facilities, which may have children
    for i,x in enumerate(facilities):
       thisproperty = x[3]
       X = []
       if thisproperty.meta.has_key('known_plugins'):
          for name_of_plugin in thisproperty.meta['known_plugins']:
              plugin = import_plugin(normalize_plugin_name( name_of_plugin, x[0] )) 
              y = introspect(plugin)
              X.append(y)
       children.append([thisproperty,X])
       if hasattr(thisproperty, 'factory') and thisproperty.factory is not None:
          plugin = import_plugin(normalize_plugin_name(thisproperty.factory.__module__, thisproperty.factory.__name__))
          y = introspect(plugin)
          X.append(y)

    # now the "others" which aren't Facilities but are inventoried
    #for i,x in enumerate(others):
    #   children.append([x[3],[]])

    return [rootobj, children]

def getname(o):
    try:
        return o.name
    except AttributeError:
        return o.__name__

def tree_display(v, prefix = ''):
    """
 Displays the result from introspect. It also serves as a reference
 on how to traverse the output of introspect.
    """
    if v == None:
        return
    if type(v) != list:
        # This is a property. Just display the name + tip ?
        tip = ''
        if v.meta.has_key('tip'):
            tip = '[TIP : %s]' % v.meta['tip']
        print '%s%s %s' % (prefix , getname(v), tip)
    else:
        root = v[0]
        print '%s%s %s' % (prefix , getname(root), type(root))
        #
        children  = v[1]
        prefix += '    '
        for child in children:
            tree_display(child, prefix)
    return

def import_app(pyfile):
    import os, sys
    if os.path.exists(pyfile):
       path, py = os.path.split(pyfile)
       modname = os.path.splitext(py)[0]
       sys.path.append(path)
       mod = __import__(modname)
       return mod
    else:
       print "no such file: %s" % pyfile
       return

def get_pyre_Apps(mod, appsuffix = 'app'):
    apps = filter(lambda name: name.lower().endswith(appsuffix), dir(mod))
    # if I get nothing... then try to see if there is a class whose name is the same as the 
    # module modulo case.
    if apps == []:
        apps = filter(lambda name: name.lower().startswith(mod.__name__.lower()), dir(mod))
    return [mod.__dict__[x] for x in apps]

def get_defaults(v):
    root = v[0]
    children = v[1]
    defaults = {}
    for child in children:
        if type(child) != list:
            defaults[child.name] = child.default
        else:
            facility = child[0]
            if hasattr(facility, 'default') and facility.default is not None:
                if type(facility.default) == str:
                    defaults[facility.name] = facility.default
                else:
                    defaults[facility.name] = facility.default.name
                #print "HELLO %s : %s" %(facility.name,  facility.default.name), facility
            elif hasattr(facility, 'factory') and facility.factory is not None:
                defaults[facility.name] = facility.factory.__module__
                #print "HELLO %s : %s" %(facility.name,  facility.factory.__module__)
            else:
                defaults[getname(facility)] = getname(facility)
    return defaults


############################################################################################
# New ... functions below attempt to use pyre for facility loading
############################################################################################

def property_default(o):
    """Tries to get the default value of a pyre Property"""
    if hasattr(o, 'default'):
        x = o.default
        if hasattr(x, 'name'):
            return x.name
        else:    
            return x
    elif hasattr(o, 'name'):
        return o.name
    elif hasattr(o, '__name__'):
        return o.__module__
    else:
        return str(o)

def facility_default(o):
    """Tries to get the default value of a pyre Facility (component)"""
    if hasattr(o, 'default') and o.default is not None:
        if type(o.default) == str:
            return o.default
        else:
            return o.default.name
    elif hasattr(o, 'factory') and o.factory is not None:
        return "<<Factory>> %s" % o.factory.__module__
    return str(o)


def prerun(pyreapp, *args, **kwargs):
    # the preamble in Application.run.
    registry = pyreapp.createRegistry()
    pyreapp.registry = registry
 
    # command line
    help, pyreapp.argv = pyreapp.processCommandline(registry)

    # curator
    curator = pyreapp.createCurator()
    pyreapp.initializeCurator(curator, registry)
 
    # look for my settings
    pyreapp.initializeConfiguration()
 
    # give descendants an opportunity to collect input from other (unregistered) sources
    pyreapp.collectUserInput(registry)
 
    print "registry: ", registry
 
    # update user options from the command line
    pyreapp.updateConfiguration(registry)
 
    return

def get_properties_and_facilities(pyreapp):
    """
Get the properties and facilities of a pyre object by looking into the traitRegistry of inventory
    """
    rootobj = pyreapp

    # If it is a pyre script or app, needs to call prerun first for initialization
    if hasattr(rootobj, 'processCommandline') and rootobj.inventory._priv_curator is None:
        prerun(pyreapp)

    # find attributes of inventory
    attnames = filter(lambda name: visibleitem(name), rootobj.inventory._traitRegistry.keys())
  
    properties = []
    facilities = []

    for name in attnames:
      if hasattr(rootobj.Inventory, name):
        val = rootobj.inventory._traitRegistry[name]
        typeval = type(val)
        if issubclass(typeval, Property):
            properties.append(val)
        elif issubclass(typeval, Facility):
            facilities.append(val)

    properties.sort(key = lambda x: x.name)
    facilities.sort(key = lambda x: x.name)

    return (properties, facilities)

def get_pf_defaults(properties, facilities):
    defaults = {}
    for property in properties:
        defaults[property.name] = property.default
    for facility in facilities:
        if hasattr(facility, 'default') and facility.default is not None:
            if type(facility.default) == str:
                defaults[facility.name] = facility.default
            else:
                defaults[facility.name] = facility.default.name
        elif hasattr(facility, 'factory') and facility.factory is not None:
            defaults[facility.name] = facility.factory.__module__
        else:
            defaults[getname(facility)] = getname(facility)
    return defaults

def getmeta(pyreapp, name, metaname):
    """
 Get meta of pyre components or inventories by name ('tip','known_plugins', etc.)
 will return empty list if he tip doesn't exist. Exception if the attribute (given in <<name>>)
 does not exist.
    """
    a = getattr(pyreapp.Inventory, name)
    try: 
        return a.meta[metaname]
    except:
        return []
         

def get_tips(pyreapp, prefix=''):
    """ Provides a reference on how the output of get_properties_and_facilities is traversed"""

    def retrieve(name, plugin):
        # this is to catch the case when the component's default is passed an instance, not a string.
        # e.g., func = pyre.inventory.facility('func', default='zero')
        #  vs.  func = pyre.inventory.facility('func', default=zero.func())
        # Question: Are both acceptable ? I don't know what the actual specification is.
        if isinstance(plugin, basestring):
            return retrieve_plugin(pyreapp, name, plugin)
        else:
            return plugin

    def meta(name, metaname):
        return getmeta(pyreapp, name, metaname)

    pf = get_properties_and_facilities(pyreapp)

    print prefix + "[%s]"  % pyreapp.name
    tab = '    '
    prefix = prefix + tab
 
    # properties are easy
    for p in pf[0]:
        print prefix+"Property [%s] : Tip -- %s" % (p.name, meta(p.name, 'tip'))

    # facilities
    for p in pf[1]:
        facility = p.name
        print prefix+"Facility [%s] : Tip -- %s" % (facility, meta(facility, 'tip'))

        # retrieve all plugins (first from known_plugins)
        plugins = meta(facility, 'known_plugins')
        if plugins is None:
            plugins = []

        # Then see if there is a default attribute
        if hasattr(p, 'default'):
            # note.. there is a chance that p.default is not a name, but an actual instance
            plugins.append(p.default)

        # attempt to do a "unique" on the plugin names
        plugins = list(set(plugins))
        plugins.sort()

        # now, instantiate them all by name:
        plugin_objs = [retrieve(facility, plugin) for plugin in plugins]

        if hasattr(p, 'factory') and p.factory is not None:
            plugin_objs.append(p.factory())

        completed = {}
        for p in plugin_objs:
            # as a last chance to make sure the components are done only once
            # duplicates are possible the default may not be passed by name. (see comments
            # after the local retrieve function
            if hasattr(p,'name') and not completed.has_key(p.name):
                get_tips(p, prefix+tab)
                completed[p.name] = 1
    return
      
############################################################################################

def test():
    #mod = import_app('parallel_map.py')
    mod = import_app('sudoku_solver.py')
    return introspect(get_pyre_Apps(mod)[0])
    
if __name__=='__main__':
    import sys
    if len(sys.argv) == 1:
        mod = import_app('sudoku_solver.py')
    else:
        mod = import_app(sys.argv[1])

    apps = get_pyre_Apps(mod) 
    X = []
    for app in apps:
        print "Tree_display"
        try:
            x = introspect(app())
            X.append(x)
            tree_display(x)
        except:
            print "WARNING *******  OLD STYLE introspect failed. ********"

        print ""
        print "by get_tips"
        get_tips(app())



# version
__id__ = "$Id: introspect.py,v 1.1 2006/08/04 00:46:30 patrickh Exp $"

# End of file
