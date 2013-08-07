<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
Editing Profile: ${profile.profile}

% if profile_records:
<table class="table table-striped table-bordered">
<tr><th>Profile</th><th>Notes</th><th>Detail</th><th>Actions</th></tr>
% for record in profile_records:
<tr><td>${record.name}</td><td>${record.record_type}</td><td>${record.contents}</td>
<td><a class="btn btn-primary" href="${request.route_path('apex_route53_profile_edit_record', id=profile.id, record_id=record.id)}">Edit</a> <a class="btn btn-danger" href=" ${request.route_path('apex_route53_profile_delete', id=profile.id, record_id=record.id)}">Delete</a></td>
</tr>
% endfor
</table>
% endif

${form.render()|n}

</%def>
