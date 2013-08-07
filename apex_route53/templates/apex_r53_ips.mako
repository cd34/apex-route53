<%inherit file="apex_r53_template.mako"/>

<%def name="body()">
% if ips:
<table class="table table-striped table-bordered">
<tr><th>IP Address</th><th>Webhost</th><th>Note</th><th>Actions</th></tr>
% for ip in ips:
<tr><td>${ip.ip_address}</td>
<td><a href="${ip.provider.url}" target="_blank">${ip.provider.name}</a></td>
<td>${ip.note}</td>
<td><i class="icon-th-list"></i><td><a class="btn btn-primary" href="${request.route_path('apex_route53_ips_edit', id=ip.id)}">Edit</a> <a class="btn btn-danger" href=" ${request.route_path('apex_route53_ips_delete', id=ip.id)}">Delete</a></td>

</tr>
% endfor
</table>
% endif

% if form:
${form.render()|n}
% endif
</%def>
