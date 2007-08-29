% tc = ""
% for trait in c.inventory.traits():
%   tc += "<tr>"
%   tc += "<td> %s </td>" % c.traitLabelFactory( trait )
%   tc += "<td> %s </td>" % c.inputBoxFactory( trait )
%   tc += "<td> %s </td>" % c.setButtonFactory( trait ) 
%   tc += "</tr>"
% pass


<div id="bd">
<div class="yui-g">


<div class="rst-doc">

<div class="section">
<h1><% c.inventory.name() %>'s inventory</h1>

<% h.form(h.url(todo='setInventory', url=c.url), method='post') %>

<table border="0">

<% tc %>

</table>

</div>

<div class="section">
<input type="submit" value="OK" name="OK"' />
<input type="submit" value="Cancel" name="Cancel"' />
</div>

<% h.end_form() %>

</div> <!--rst-doc-->


</div>
</div>
