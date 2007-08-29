% controller = c.controller
% controller_name = controller.get_controller_name()
% def link( appname ): # this is a bad implementation. somehow "h.url" does not work and I have to use this hack
%   url = "/%s/%s" % (controller_name, appname)
%   return '<a href="%s">%s</a>' % (url, appname)
% def td( s ): return "<td>%s</td>" % s
% def tr( s ): return "<tr>%s</tr>" % s
% texts = []
% reg = c.pyreapp_registry
% for appname in reg:
%   cells = [ link( appname ) ]
%   cells =  [ td( c1 ) for c1 in cells ]
%   text = tr(  td("&nbsp"*2).join( cells )  )
%   texts.append( text )
% pass


<div id="bd">
<div class="yui-g">


<div class="rst-doc">

<h1 class="pudge-member-page-heading">
Pyre applications
</h1>


<table border="0">

<% '\n'.join(texts) %>

</table>


</div> <!--rst-doc-->


</div>
</div>
