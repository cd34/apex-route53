<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>Delete ${zone.name}?</h2>
<table class="table table-striped table-bordered">
<tr><th>Zone</th><th>Record Type</th><th>Contents</th></tr>
% for record_set in zone.record_sets:
<tr><td>${record_set.name}</td><td>${record_set.rrset_type}</td>
<td>
% for content in record_set.records:
${content}<br/>
% endfor
</td>
</tr>
% endfor
</table>

${form.render()|n}
</%def>
