<%namespace file="apex:templates/flash_template.mako" import="*"/>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>${self.page_title()}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
${self.head_css()}
  </head>
  <body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
  <div class="container">
    <a class="navbar-brand" href="/">Route53 DNS Manager</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_index')}">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_dns_list')}">DNS List</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_domain_add')}">Add Domains</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_profiles')}">Profiles</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_registrars')}">Registrars</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_ips')}">IP Addresses</a></li>
        <li class="nav-item"><a class="nav-link" href="${request.route_path('apex_route53_webhosts')}">Webhosts</a></li>
      </ul>
    </div>
  </div>
</nav>

<div class="container" style="padding-top: 80px;">
  <div class="row">
    <div class="col">
${apex_flash()}
<h2>${self.page_title()}</h2>

${self.body()}
    </div>
  </div>
</div>

<script src="//cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
${self.foot_js()}
  </body>
</html>

<%def name="page_title()">
% if title:
${title}
% endif
</%def>

<%def name="head_css()">
</%def>

<%def name="head_js()">
</%def>

<%def name="foot_js()">
</%def>
