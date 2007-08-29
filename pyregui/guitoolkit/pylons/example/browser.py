from arcs.lib.base import *

import os
default_open_file = os.path.expanduser( '~' )
default_write_file = os.path.expanduser( '~' )


class BrowserController(BaseController):
    
    def index(self, purpose='readfile', url = None):
        environ = request.environ
        remote_host = environ.get('REMOTE_HOST')
        if  remote_host != "localhost": raise "only local connection is allowed"

        print purpose, url
        return getattr(self, purpose)( url )


    def readfile(self, path):
        if path is None: path = default_open_file
        else: path = eval( path )
        print path
        c.path = path
        return render_response( "/browser/readfile.myt" )


    def writefile(self, path):
        if path is None: path = default_write_file
        else: path = eval( path )
        print path
        c.path = path
        return render_response( "/browser/writefile.myt" )


    def browse(self, path):
        print path
        if path is None: path = default_write_file
        else: path = path[1:]
        c.path_to_public_dir = self._path_to_public_dir()
        c.path =  path 
        return render_response( "/browser/browse.myt" )


    def serve_raw(self, path):
        import os
        limit = 10000000L
        print path
        path = path[1:]
        if os.path.getsize(path) > limit: raise "%s: file size too large" % path
        t = open(path).read()
        return Response( t )
    

    def picked(self, path):
        path = eval(path)
        returnurl = session['returnurl']
        print returnurl
        session['browser-pick'] = path
        session['default_open_file'] = path
        session.save()
        return redirect_to( returnurl )


    def _path_to_public_dir(self):
        import os
        curdir = os.path.abspath( os.path.dirname( __file__ ) )
        return os.path.abspath( os.path.join( curdir, '..', 'public' ) )

    pass # end of BrowserController


