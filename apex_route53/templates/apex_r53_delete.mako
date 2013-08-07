<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>Your Domains</h2>
<table class="table table-striped table-bordered">
<tr><th>Zone</th><th>Registrar</th><th>Actions</th></tr>
% for zone in zones:
<tr><td>${zone.name}</td><td>registrar</td><td><a class="btn btn-primary" href="${request.route_path('apex_route53_edit', id=zone.id)}">Edit</a> <a class="btn btn-danger" href=" ${request.route_path('apex_route53_delete', id=zone.id)}">Delete</a></td></tr>
% endfor:
</table>

<a class="btn btn-success">Add Domain</a>
</%def>
