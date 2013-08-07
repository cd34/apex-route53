<%inherit file="apex_r53_template.mako"/>

<%def name="body()">
% if providers:
<table class="table table-striped table-bordered">
<tr><th>Registrar</th><th>Actions</th></tr>
% for provider in providers:
<tr><td><a href="${provider.url}" target="_blank">${provider.name}</a></td>
<td>${['','Debian'][provider.os]}</td><td>Edit Delete</td></tr>
% endfor
</table>
% endif

% if form:
${form.render()|n}
% endif
</%def>
