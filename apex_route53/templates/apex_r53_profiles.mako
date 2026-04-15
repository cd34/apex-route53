<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
% if profiles:
<table class="table table-striped table-bordered">
<thead>
<tr><th>Profile</th><th>Notes</th><th>Actions</th></tr>
</thead>
<tbody>
% for profile in profiles:
<tr><td>${profile.profile}</td><td>${profile.note}</td>
<td><a class="btn btn-primary btn-sm" href="${request.route_path('apex_route53_profile_edit', id=profile.id)}">Edit</a> <a class="btn btn-danger btn-sm" href="${request.route_path('apex_route53_profile_delete', id=profile.id)}">Delete</a></td>
</tr>
% endfor
</tbody>
</table>
% endif

${form.render()|n}

</%def>
