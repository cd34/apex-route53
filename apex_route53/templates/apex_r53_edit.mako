<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>${zone.name}</h2>
<table class="table table-striped table-bordered">
<tr><th>Zone</th><th>Record Type</th><th>Contents</th><th>Detail</th><th>Actions</th></tr>
% for record_set in zone.record_sets:
<!--tr><td colspan="5">${record_set._initial_vals.items()}<br/>${record_set.uniq}</td></tr-->
<tr><td>${record_set.name}</td><td>${record_set.rrset_type}</td>
<td>
% for content in record_set.records:
${content}<br/>
% endfor
</td><td><i class="icon-th-list"></i><td><a class="btn btn-primary" href="${request.route_path('apex_route53_edit_rs', id=zone.id, recordset_id=record_set.uniq)}">Edit</a> <a class="btn btn-danger" href=" ${request.route_path('apex_route53_delete_rs', id=zone.id, recordset_id=record_set.uniq)}">Delete</a></td></tr>
% endfor
</table>
</%def>
