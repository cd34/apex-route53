from sqlalchemy import engine_from_config

from apex_route53.models import initialize_sql
from apex_route53.views import (domain_add,
                                delete,
                                delete_rs,
                                dns_list,
                                edit,
                                edit_rs,
                                index,
                                ips,
                                ips_edit,
                                ips_delete,
                                profiles,
                                profile_edit,
                                profile_delete,
                                registrars,
                                webhosts,
                                webhosts_edit,
                                webhosts_delete,
                               )

def includeme(config):
    settings = config.registry.settings

    initialize_sql(engine_from_config(settings, 'sqlalchemy.'), settings)

    config.add_translation_dirs('apex:locale/')
    config.add_static_view('apex_route53/static', 'apex_route53:static')

    if not settings.get('mako.directories'):
        config.add_settings({'mako.directories': ['apex_route53:templates']})

    """
    render_template = settings['apex.apex_render_template'
                              ] = settings.get('apex.apex_r53_template',
                                               'apex_route53:templates/apex_r53_template.mako')
    """

    config.add_route('apex_route53_index', '/')
    config.add_view(index, route_name='apex_route53_index',
                    renderer='apex_route53:templates/apex_r53_index.mako',
                    permission='authenticated')

    config.add_route('apex_route53_dns_list', '/dns_list')
    config.add_view(dns_list, route_name='apex_route53_dns_list',
                    renderer='apex_route53:templates/apex_r53_dns_list.mako',
                    permission='authenticated')

    config.add_route('apex_route53_domain_add', '/domain/add')
    config.add_view(domain_add, route_name='apex_route53_domain_add',
                    renderer='apex_route53:templates/apex_r53_domain_add.mako',
                    permission='authenticated')

    config.add_route('apex_route53_edit', '/edit/:id')
    config.add_view(edit, route_name='apex_route53_edit',
                    renderer='apex_route53:templates/apex_r53_edit.mako',
                    permission='authenticated')

    config.add_route('apex_route53_edit_rs', '/edit/:id/:recordset_id')
    config.add_view(edit_rs, route_name='apex_route53_edit_rs',
                    renderer='apex_route53:templates/apex_r53_edit_rs.mako',
                    permission='authenticated')

    config.add_route('apex_route53_delete', '/delete/:id')
    config.add_view(delete, route_name='apex_route53_delete',
                    renderer='apex_route53:templates/apex_r53_delete.mako',
                    permission='authenticated')

    config.add_route('apex_route53_delete_rs', '/delete/:id/:recordset_id')
    config.add_view(delete_rs, route_name='apex_route53_delete_rs',
                    renderer='apex_route53:templates/apex_r53_delete_rs.mako',
                    permission='authenticated')

    config.add_route('apex_route53_profiles', '/profiles')
    config.add_view(profiles, route_name='apex_route53_profiles',
                    renderer='apex_route53:templates/apex_r53_profiles.mako',
                    permission='authenticated')

    config.add_route('apex_route53_profile_edit', '/profiles/:id')
    config.add_view(profile_edit, route_name='apex_route53_profile_edit',
                renderer='apex_route53:templates/apex_r53_profile_edit.mako',
                permission='authenticated')

    config.add_route('apex_route53_profile_edit_record', 
                     '/profiles/:id/:record_id')
    config.add_view(profile_edit, 
            route_name='apex_route53_profile_edit_record',
            renderer='apex_route53:templates/apex_r53_profile_edit.mako',
            permission='authenticated')

    config.add_route('apex_route53_profile_delete', 
                     '/profiles/:id/delete')
    config.add_view(profile_delete, route_name='apex_route53_profile_delete',
                renderer='apex_route53:templates/apex_r53_profile_delete.mako',
                permission='authenticated')

    config.add_route('apex_route53_registrars', '/registrars')
    config.add_view(registrars, route_name='apex_route53_registrars',
                    renderer='apex_route53:templates/apex_r53_registrars.mako',
                    permission='authenticated')

    config.add_route('apex_route53_ips', '/ips')
    config.add_view(ips, route_name='apex_route53_ips',
                    renderer='apex_route53:templates/apex_r53_ips.mako',
                    permission='authenticated')

    config.add_route('apex_route53_ips_edit', '/ips/:id')
    config.add_view(ips_edit, route_name='apex_route53_ips_edit',
                    renderer='apex_route53:templates/apex_r53_ips_edit.mako',
                    permission='authenticated')

    config.add_route('apex_route53_ips_delete', '/ips/:id/delete')
    config.add_view(ips_delete, route_name='apex_route53_ips_delete',
                    renderer='apex_route53:templates/apex_r53_ips_delete.mako',
                    permission='authenticated')

    config.add_route('apex_route53_webhosts', '/webhosts')
    config.add_view(webhosts, route_name='apex_route53_webhosts',
                    renderer='apex_route53:templates/apex_r53_webhosts.mako',
                    permission='authenticated')

    config.add_route('apex_route53_webhosts_edit', '/webhosts/:id')
    config.add_view(webhosts_edit, route_name='apex_route53_webhosts_edit',
                    renderer='apex_route53:templates/apex_r53_webhosts_edit.mako',
                    permission='authenticated')

    config.add_route('apex_route53_webhosts_delete', '/webhosts/:id/delete')
    config.add_view(webhosts_delete, route_name='apex_route53_webhosts_delete',
                    renderer='apex_route53:templates/apex_r53_webhosts_delete.mako',
                    permission='authenticated')

