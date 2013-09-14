from wtforms import (RadioField,
                     SelectField,
                     SelectMultipleField,
                     TextField,
                     validators)

from apex import MessageFactory as _
from apex.lib.form import ExtendedForm

from apex_route53.lib import domain_re

class RegistrarForm(ExtendedForm):
    """ Registrar Form
    """
    registrar = TextField(_('Registrar'), [validators.Required(), \
                         validators.Length(min=4, max=25)])
    url = TextField(_('URL'), [validators.Required(), \
                         validators.Length(min=4, max=80)])

class IPForm(ExtendedForm):
    """ Registrar Form
    """
    ip_address = TextField(_('IP Address'), [validators.Required(), \
        validators.Length(min=4, max=60)])
    provider_id = SelectField(_('Web Host'), [validators.Required()], \
        coerce=int)
    note = TextField(_('Note'))

class ProviderForm(ExtendedForm):
    """ Registrar Form
    """
    name = TextField(_('Web Host'), [validators.Required(), \
                         validators.Length(min=4, max=25)])
    url = TextField(_('URL'), [validators.Required(), \
                         validators.Length(min=4, max=80)])
    os = SelectField(_('Operating System'), [validators.Required()],
                   choices=[('1','Debian')])

class DNS_A_Form(ExtendedForm):
    """ 
    """
    name = TextField(_('Name'))
    type = SelectField(_('Record Type'), [validators.Required()],
               choices=[('A','A - IPv4 Address')])
    alias = RadioField(_('Alias'), [validators.Required()],
               choices=[('Y','Yes'), ('N', 'No')])
    ttl = TextField(_('TTL'))
    value = SelectMultipleField(_('IP Addresses'))
    #routing_policy = SelectField(_('Routing Policy'), [validators.Required()],
    #           choices=[('simple', 'Simple')])

class DomainForm(ExtendedForm):
    profile_id = SelectField(_('Profile'), coerce=int)
    ip_id = SelectField(_('IP Addresses'), coerce=int)
    domain = TextField(_('Domain'), [validators.Required(), \
                         validators.Length(min=4, max=64), \
                         validators.Regexp(domain_re, \
                         message=_('invalid domain'))])

class YesNoForm(ExtendedForm):
    yesno = SelectField(_('Yes or No'), [validators.Required(), 
               validators.AnyOf(['Y'], message='Must Select Yes')],
               choices=[('N', 'No'), ('Y','Yes')])

class ProfileForm(ExtendedForm):
    """ Profile Form
    """
    profile = TextField(_('Profile'), [validators.Required(), \
                         validators.Length(min=4, max=25)])
    note = TextField(_('Note'))

class ProfileRecordForm(ExtendedForm):
    """ Profile Record Form
    """
    record_type = SelectField(_('Record Type'), [validators.Required()],
               choices=[('A', 'A'), ('MX', 'MX'), ('SPF', 'SPF'), 
               ('TXT', 'TXT')])
    name = TextField(_('Hostname'))
    contents = TextField(_('Contents'), [validators.Required(), \
                         validators.Length(min=4, max=25)])
