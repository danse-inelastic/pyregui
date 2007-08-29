#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class Option:
    
    def __init__(self, name, default, description):
        self.name = name
        self.default = default
        self.description = description
        return

    pass # end of Option


from pyregui.inventory.proxies.InventoryProxy import InventoryProxy


class HelperAdaptor:

    def init(self): return
    def fini(self): return

    def main(self, appname, verbosity = 1):
        self.verbosity = verbosity
        invp = InventoryProxy( self.inventory )
        app_info = self.name, self.__class__.__doc__
        options = [(app_info,  self._getOptions( '', invp ))]
        for fac in invp.facilities(self.verbosity):
            component = fac.component()
            opts = self._getOptions_r( '', component )
            options += opts
            continue
        
        cmdtokens = [appname]
        for comp_info, opts in options:
            for opt in opts:
                cmdtokens.append( 
                    '--%s=%r' % (opt.name, opt.default) )
                continue
            continue
        fullcmd = ' '.join( cmdtokens )

        pre = [
            "NAME",
            "  %s" % (appname,),
            "",
            "SYNOPSIS",
            "  %s [options]" % appname,
            "",
            "Command With All Options And Their Defaults:",
            "  %s" % fullcmd,
            "",
            "",
            "ALL OPTIONS",
            " General Description",
            "  All options are in the form",
            "    --<component>.<property>=<value>",
            "  In the following, a description of the component",
            "  will be given first, and then all options of that",
            "  component will be presented.",
            "",
            "",
            ]

        print '\n'.join( pre )
        
        self._printOptions( options )
        return
    

    def _getOptions_r(self, prefix, component):
        inventory = component.inventory
        invp = InventoryProxy( inventory )
        
        ret = []
        if prefix == '': name = invp.name()
        else: name = '.'.join( [prefix, invp.name() ] )
        component_info = name, component.__class__.__doc__
        opts = self._getOptions( name, invp )
        ret.append( (component_info, opts) )
        for fac in invp.facilities(self.verbosity):
            component = fac.component()
            opts = self._getOptions_r( name, component )
            ret += opts
            continue
        return ret
    

    def _getOptions(self, prefix, invp):
        ret = []
        for prop in invp.properties(verbosity = self.verbosity):
            name = prop.name()
            if prefix == '' : n = name
            else: n = '.'.join( [ prefix, name ] )
            opt = Option( n, prop.value(), prop.tip() )
            ret.append(opt)
            continue
        return ret


    def _printOptions( self, options ):
        for comp_info, opts in options:
            name, description = comp_info
            if description is None:
                description = "Please consider writing a python docstring"
            print "\n* Component '%s':\n%s\n" % (name, description)
            
            if len(opts): print "Options:\n"
            for opt in opts:
                description = opt.description.split( '\n' )
                description = '\n'.join(
                    [ '\t'+d.strip() for d in description ] )
                print "--%s=%r\n%s" % (
                    opt.name, opt.default, description)
                print
                continue
            continue
        return

    pass # end of HelperAdaptor


from pyregui.pyreui import getPyreApp, findExecutable


def help(appname, classname = None, verbosity = 1):
    if not isinstance (appname, basestring ) or len(appname) == 0:
        raise RuntimeError, "pyre application is not supplied. %s" % _h
    exe = findExecutable( appname )
    #print exe
    App = getPyreApp( exe, None )
    class T(HelperAdaptor, App):
        __doc__ = App.__doc__
        pass
    t = T()
    t.run(appname, verbosity)
    return



_h = """Enter
  pyreapphelp.py -h
for help
"""


def main():
    import sys
    from optparse import OptionParser
    
    parser = OptionParser(
        "usage: %prog [options] -a PYREAPP [pyreapp-options] ")
    parser.add_option(
        '-v', '--verbosity', dest = 'verbosity', type = 'int',  default = '1',
        help = 'When verbosity is increased, more advanced options will show up' )
    parser.add_option(
        '-a', '', dest = 'pyreapp', 
        help = 'pyre application' )

    argv = sys.argv
    helpargv, appargv = _splitArgv(argv)
    opts, args = parser.parse_args(helpargv)
    appname = opts.pyreapp
    classname = None
    sys.argv = appargv
    import journal
    journal.error( 'pyre.inventory' ).deactivate()
    verbosity = opts.verbosity
    help( appname, classname, verbosity)
    return


def _splitArgv( argv ):
    try:
        n = argv.index( '-a' ) + 1
    except:
        n = len(argv) + 1
    return argv[1:n+1] , argv[n:]


# main
if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
