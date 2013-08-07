<%inherit file="apex_r53_template.mako"/>

<%def name="body()">
% if registrars:
<table class="table table-striped table-bordered">
<tr><th>Registrar</th><th>Actions</th></tr>
% for registrar in registrars:
<tr><td><a href="${registrar.url}" target="_blank">${registrar.registrar}</a></td>
<td>Edit Delete</td></tr>
% endfor
</table>
% endif

% if form:
${form.render()|n}
% endif
</%def>
