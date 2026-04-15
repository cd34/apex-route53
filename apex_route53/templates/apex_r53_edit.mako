<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>${zone.name}</h2>
<table class="table table-striped table-bordered">
<thead>
<tr><th>Zone</th><th>Record Type</th><th>Contents</th><th>Actions</th></tr>
</thead>
<tbody>
% for record_set in zone.record_sets:
<tr><td>${record_set.name}</td><td>${record_set.rrset_type}</td>
<td>
% for content in record_set.records:
${content}<br/>
% endfor
</td>
<td>
% if record_set.rrset_type not in ['SOA','NS']:
<a class="btn btn-primary btn-sm" href="${request.route_path('apex_route53_edit_rs', id=zone.id, recordset_id=record_set.uniq)}">Edit</a> <a class="btn btn-danger btn-sm" href="${request.route_path('apex_route53_delete_rs', id=zone.id, recordset_id=record_set.uniq)}">Delete</a>
% endif
</td></tr>
% endfor
</tbody>
</table>

<h3>Delete this zone?</h3>
${form.render()|n}
</%def>
