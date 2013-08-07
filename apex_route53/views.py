from apex_route53.lib import route53_connect

from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from apex.lib.db import merge_session_with_post
from apex.lib.flash import flash

from apex.models import DBSession
from apex_route53.forms import (DomainForm,
                                DNS_A_Form,
                                IPForm,
                                ProfileForm,
                                ProfileRecordForm,
                                ProviderForm,
                                RegistrarForm,
                               )
from apex_route53.lib import (get_ip,
                              get_ips,
                              get_ips_choices,
                              get_profile,
                              get_profiles,
                              get_profiles_choices,
                              get_profile_record,
                              get_profile_records,
                              get_providers,
                              get_registrars,
                             )
from apex_route53.models import (IP,
                                 Profile,
                                 Profile_Record,
                                 Provider,
                                 Registrar,
                                )

def index(request):
    amazon_aws = route53_connect()
    zones = amazon_aws.list_hosted_zones()
    return {'title':'Your domains', 'zones':zones}

def dns_list(request):
    amazon_aws = route53_connect()
    zones = amazon_aws.list_hosted_zones()
    return {'title':'Your domains', 'zones':zones}

def edit(request):
    amazon_aws = route53_connect()
    zone = amazon_aws.get_hosted_zone_by_id(request.matchdict['id'])
    return {'zone':zone}

def delete(request):
    amazon_aws = route53_connect()
    zones = amazon_aws.list_hosted_zones()
    return {'zones':zones}

def domain_add(request):
    form = DomainForm(request.POST)
    form.ip_id.choices = get_ips_choices()
    form.profile_id.choices = get_profiles_choices()
    if request.method == 'POST' and form.validate():
        amazon_aws = route53_connect()
        if not request.POST['domain'].endswith('.'):
            request.POST['domain'] = '{0}.'.format(request.POST['domain'])
        zone, change_info = amazon_aws.create_hosted_zone( \
            request.POST['domain'])
        ip = get_ip(request.POST['ip_id'])
        profile_records = get_profile_records(request.POST['profile_id'])
        for record in profile_records:
            contents = [record.contents.replace('_IP_', ip.ip_address)]
            name = request.POST['domain']
            if record.name:
                name = '{0}.{1}'.format(record.name, request.POST['domain'])

            if record.record_type == 'A':
                new_zone, change_info = zone.create_a_record(name=name, \
                    values=contents)
                new_zone.save()
            if record.record_type == 'AAAA':
                new_zone, change_info = zone.create_aaaa_record(name=name, \
                    values=contents)
            if record.record_type == 'MX':
                new_zone, change_info = zone.create_mx_record(name=name, \
                    values=contents)
                new_zone.save()
            if record.record_type == 'SPF':
                new_zone, change_info = zone.create_spf_record(name=name, \
                    values=contents)
                new_zone.save()

    return {'title':'Add Domain', 'form':form}

def profiles(request):
    form = ProfileForm(request.POST)
    if request.method == 'POST' and form.validate():
        record = Profile()
        record = merge_session_with_post(record, request.POST.items())
        DBSession.merge(record)
        DBSession.flush()
        return HTTPFound(location= \
            route_url('apex_route53_profiles', request))
    return {'title':'Profiles', 'form':form, 'profiles':get_profiles()}

def profile_edit(request):
    form = ProfileRecordForm(request.POST)
    if 'record_id' in request.matchdict:
        record = get_profile_record(request.matchdict['id'], \
            request.matchdict['record_id'])
        if not request.POST:
            form.record_type.data = record.record_type
            form.name.data = record.name
            form.contents.data = record.contents
    else:
        record = Profile_Record(profile_id=request.matchdict['id'])

    if request.method == 'POST' and form.validate():
        if request.POST['record_type'] in ['TXT', 'SPF']:
            request.POST['contents'] = '"' + request.POST['contents'] \
                .replace('"','') + '"'
        record = merge_session_with_post(record, request.POST.items())
        DBSession.merge(record)
        DBSession.flush()
        return HTTPFound(location= \
            route_url('apex_route53_profile_edit', request, \
            id=request.matchdict['id']))
    return {'title':'Edit Profile Records', \
        'form':form, \
        'profile':get_profile(request.matchdict['id']), \
        'profile_records':get_profile_records(request.matchdict['id'])}

def profile_delete(request):
    record = get_profile_record(request.matchdict['id'], \
        request.matchdict['record_id'])
    DBSession.delete(record)
    DBSession.flush()
    return HTTPFound(location= \
        route_url('apex_route53_profile_edit', request, \
        id=request.matchdict['id']))

def registrars(request):
    form = RegistrarForm(request.POST)
    registrars = get_registrars()
    record = Registrar()

    if request.method == 'POST' and form.validate():
        record = merge_session_with_post(record, request.POST.items())
        DBSession.merge(record)
        DBSession.flush()
        return HTTPFound(location= \
            route_url('apex_route53_registrars', request))
    return {'title':'Registrars', 'form':form, 'registrars':registrars}

def ips(request):
    providers = get_providers()
    ips = get_ips()
    if not providers:
        flash('You have no providers defined, please add at least one')
        return HTTPFound(location=route_url('apex_route53_webhosts', request))
    form = IPForm(request.POST, providers=providers)
    form.provider_id.choices = providers
    record = IP()

    if request.method == 'POST' and form.validate():
        record = merge_session_with_post(record, request.POST.items())
        DBSession.merge(record)
        DBSession.flush()
        return HTTPFound(location= \
            route_url('apex_route53_ips', request))
    return {'title':'IP Addresses', 'form':form, 'ips':ips}

def ips_edit(request):
    return {}

def ips_delete(request):
    return {}

def webhosts(request):
    form = ProviderForm(request.POST)
    providers = DBSession.query(Provider).order_by(Provider.name).all()
    record = Provider()

    if request.method == 'POST' and form.validate():
        record = merge_session_with_post(record, request.POST.items())
        DBSession.merge(record)
        DBSession.flush()
        return HTTPFound(location= \
            route_url('apex_route53_webhosts', request))
    return {'title':'Web Hosts', 'form':form, 'providers':providers}

def webhosts_edit(request):
    return {}

def webhosts_delete(request):
    return {}

def edit_rs(request):
    form = DNS_A_Form(request.POST)
    form.value.choices = get_ips_choices()
    amazon_aws = route53_connect()
    zone = amazon_aws.get_hosted_zone_by_id(request.matchdict['id'])
    for record_set in zone.record_sets:
        if record_set.uniq == request.matchdict['recordset_id']:
            form.name.data = record_set.name
            form.type.data = record_set.rrset_type
            form.alias.data = 'Y' if record_set.is_alias_record_set() else 'N'
            form.ttl.data = record_set.ttl
            form.value.data = record_set.records[0]
            #form.routing_policy.data = record_set.routing_policy
            # not supported in python-route53
            return {'zone':zone, 'record_set':record_set, 'form':form}
    return {}

def delete_rs(request):
    return {}
