<div id="bd">
<div class="yui-g">


<div class="rst-doc">


<h1><% c.appname %></h1>
<div class="section">
<p>
<% c.onelinehelp %>
</p>

<a href="<% c.helpurl %>"> Click here for help </a>

</div>

<div class="section">
<table border = "0" cellspacing="10" cellpadding="10">
<tr>
<td>
 <% h.button_to( "configure", h.url( appname = c.appname, todo = 'configure' ) )  %>
</td>
<td> &nbsp; &nbsp;</td>
<td>
<% h.button_to( "save configuration", h.url( appname = c.appname, todo = 'save_configuration_start' ) ) %>
</td>
</tr>

<tr>
<td> &nbsp; </td>
<td> &nbsp; </td>
<td> &nbsp; </td>
</tr>

<tr>
<td>
<% h.button_to( "run", h.url( todo='run' ) ) %>
</td>
<td> &nbsp; </td>
<td> &nbsp; </td>
</tr>
</table>
</div>

</div> <!--rst-doc-->


</div>
</div>
