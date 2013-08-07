<%inherit file="apex_r53_template.mako"/>

<%def name="title()">
</%def>

<%def name="body()">

<table id="tablesort" class="table table-striped table-bordered">
<thead>
<tr><th>Zone</th><th>DNS Servers</th></tr>
</thead>
<tbody>
% for zone in zones:
<tr><td>${zone.name}</td><td>
% for record in zone.record_sets:
% if record.rrset_type == "NS":
% for rec in record.records:
${rec[:-1]}<br/>
% endfor
% endif
% endfor
</td></tr>
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
