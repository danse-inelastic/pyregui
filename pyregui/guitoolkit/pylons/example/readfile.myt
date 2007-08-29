% import os
% def dirlink( path ):
%   name = os.path.split(path) [-1]
%   return '''<p><a href='/browser/readfile/"%s"'>%s</a></p>''' % (path, name)
% def filelink( path ):
%   name = os.path.split(path) [-1]
%   return '''<p><a href='/browser/picked/\"%s\"'>%s</a></p>''' % (path, name)
% def link(path):
%   if os.path.isdir(path): return dirlink(path)
%   return filelink( path )
%
% def ignore(path):
%   name = os.path.split( path )[-1]
%   if name.startswith( '.' ): return True
%   return False
% curfile = c.path
% import os
% if os.path.isdir( curfile ):
%   directory = curfile
% else:
%   directory = os.path.abspath( os.path.dirname( curfile ) )
% items = os.listdir( directory )
% texts = []
% for item in items:
%   path = os.path.join( directory, item )
%   if ignore(path): continue
%   text = link( path )
%   texts.append( text )
%   continue # end for
% pass



<div id="bd">
<div class="yui-g">


<div class="rst-doc">

<h1><% directory %></h1>

<% '\n'.join( texts ) %>

</div> <!--rst-doc-->


</div>
</div>
