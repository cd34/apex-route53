import re

from apex_route53.models import (DBSession,
                                 IP,
                                 Profile,
                                 Profile_Record,
                                 Provider,
                                 Registrar,
                                )

import route53

from pyramid.threadlocal import get_current_registry

domain_re = re.compile('^[a-z0-9-\.]+$')

def route53_connect():
    settings = get_current_registry().settings
    connect = route53.connect(
      aws_access_key_id = settings.get('aws_access_key_id', None),
      aws_secret_access_key = settings.get('aws_secret_access_key', None),
    )
    return connect

def get_registrars():
    return DBSession.query(Registrar). \
        order_by(Registrar.registrar).all()

def get_profile(id):
    return DBSession.query(Profile). \
        filter(Profile.id==id).one()

def get_profiles():
    return DBSession.query(Profile). \
        order_by(Profile.profile).all()

def get_profile_record(profile_id, record_id):
    return DBSession.query(Profile_Record). \
        filter(Profile_Record.profile_id==profile_id). \
        filter(Profile_Record.id==record_id).one()

def get_profile_records(profile_id):
    return DBSession.query(Profile_Record). \
        filter(Profile_Record.profile_id==profile_id). \
        order_by(Profile_Record.name).all()

def get_providers():
    return DBSession.query(Provider.id,Provider.name). \
        order_by(Provider.name).all()

def get_ip(id):
    return DBSession.query(IP). \
        filter(IP.id==id).one()

def get_ips():
    return DBSession.query(IP). \
        order_by(IP.ip_address).all()

def ip_notes(value):
    return (value[0], '%s (%s)' % (value[1], value[2]))

def get_ips_choices():
    ips = DBSession.query(IP.id, IP.ip_address, IP.note). \
        order_by(IP.ip_address).all()
    return map(ip_notes, ips)

def get_profiles_choices():
    return DBSession.query(Profile.id, Profile.profile). \
        order_by(Profile.profile).all()
