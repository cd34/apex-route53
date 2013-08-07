<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<h2>${zone.name}</h2>

${form.render()|n}

</%def>
