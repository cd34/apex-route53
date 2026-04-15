<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>${zone.name}</h2>
<table class="table table-striped table-bordered">
<thead>
<tr><th>Zone</th><th>Record Type</th><th>Contents</th></tr>
</thead>
<tbody>
<tr><td>${record_set.name}</td><td>${record_set.rrset_type}</td>
<td>
% for content in record_set.records:
${content}<br/>
% endfor
</td>
</tr>
</tbody>
</table>

${form.render()|n}

</%def>
