<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">
<table id="tablesort" class="table table-striped table-bordered">
<thead>
<tr><th>Zone</th><th>Registrar</th><th>Actions</th></tr>
</thead>
<tbody>
% for zone in zones:
<tr><td>${zone.name}</td><td>registrar</td><td><a class="btn btn-primary" href="${request.route_path('apex_route53_edit', id=zone.id)}">Edit</a> <a class="btn btn-danger" href=" ${request.route_path('apex_route53_delete', id=zone.id)}">Delete</a></td></tr>
% endfor:
</tbody>
</table>

<script>
$(document).ready(function()
    {
        $("#tablesort").tablesorter({
          sortList: [[0,0]],
        });
    }
);
</script>
</%def>

<%def name="head_js()">
<script src="${request.static_url('apex_route53:static/jquery.tablesorter.min.js')}">   
</script>
</%def> 
