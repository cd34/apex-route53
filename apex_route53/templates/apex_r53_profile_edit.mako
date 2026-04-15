<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
Editing Profile: ${profile.profile}

% if profile_records:
<table class="table table-striped table-bordered">
<thead>
<tr><th>Name</th><th>Record Type</th><th>Contents</th><th>Actions</th></tr>
</thead>
<tbody>
% for record in profile_records:
<tr><td>${record.name}</td><td>${record.record_type}</td><td>${record.contents}</td>
<td><a class="btn btn-primary btn-sm" href="${request.route_path('apex_route53_profile_edit_record', id=profile.id, record_id=record.id)}">Edit</a> <a class="btn btn-danger btn-sm" href="${request.route_path('apex_route53_profile_delete', id=profile.id, record_id=record.id)}">Delete</a></td>
</tr>
% endfor
</tbody>
</table>
% endif

${form.render()|n}

</%def>
