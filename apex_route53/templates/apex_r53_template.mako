<%namespace file="apex:templates/flash_template.mako" import="*"/>
<!DOCTYPE html>
<html>
  <head>
    <title>${self.page_title()}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">
<style>
body { padding:40px; }
</style>
    <script src="http://code.jquery.com/jquery.js"></script>
<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
${self.head_js()}
  </head>
  <body>

<div class="navbar navbar-fixed-top navbar-inverse">
  <div class="navbar-inner">
    <div class="container">
     <a class="brand" href="/">Route53 DNS Manager</a>
      <ul class="nav">
<li><a href="${request.route_path('apex_route53_index')}">Home</a></li>
<li><a href="${request.route_path('apex_route53_dns_list')}"">DNS List</a></li>
<li><a href="${request.route_path('apex_route53_domain_add')}"">Add Domains</a></li>
<li><a href="${request.route_path('apex_route53_profiles')}"">Add Profiles</a></li>
<li><a href="${request.route_path('apex_route53_registrars')}"">Add Registrars</a></li>
<li><a href="${request.route_path('apex_route53_ips')}"">Add IP Addresses</a></li>
<li><a href="${request.route_path('apex_route53_webhosts')}"">Add Webhost</a></li>
      </ul>
    </div>
  </div>
</div>
<div class="container">
  <div class="row">
${apex_flash()}
<h2>${self.page_title()}</h2>

${self.body()}
  </div>
</div>

  </body>
</html>

<%def name="page_title()">
% if title:
${title}
% endif
</%def>

<%def name="head_js()">
</%def>
