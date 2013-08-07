Apex Route53 helper

Module to work with Route53 via a web interface using Pyramid.


Minimal config for Pyramid development.ini

    mako.directories = r53:templates
    aws_access_key_id = 
    aws_secret_access_key = 
    apex.session_secret = sesh_secret
    apex.auth_secret = auths_secret
    apex.came_from_route = apex_route53_index

__init__.py:

add: 

    config.include('apex', route_prefix='/auth')
    config.include('apex_route53', route_prefix='/')

above:

    return config.make_wsgi_app()
