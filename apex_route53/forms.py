from wtforms import (RadioField,
                     SelectField,
                     SelectMultipleField,
                     StringField,
                     validators)

from apex import MessageFactory as _
from apex.lib.form import ExtendedForm

from apex_route53.lib import domain_re

class RegistrarForm(ExtendedForm):
    registrar = StringField(_('Registrar'), [
        validators.DataRequired(), validators.Length(min=4, max=25)])
    url = StringField(_('URL'), [
        validators.DataRequired(), validators.Length(min=4, max=80)])

class IPForm(ExtendedForm):
    ip_address = StringField(_('IP Address'), [
        validators.DataRequired(), validators.Length(min=4, max=60)])
    provider_id = SelectField(_('Web Host'), [validators.DataRequired()],
        coerce=int)
    note = StringField(_('Note'))

class ProviderForm(ExtendedForm):
    name = StringField(_('Web Host'), [
        validators.DataRequired(), validators.Length(min=4, max=25)])
    url = StringField(_('URL'), [
        validators.DataRequired(), validators.Length(min=4, max=80)])
    os = SelectField(_('Operating System'), [validators.DataRequired()],
        choices=[('1', 'Debian')])

class DNS_A_Form(ExtendedForm):
    name = StringField(_('Name'))
    type = SelectField(_('Record Type'), [validators.DataRequired()],
        choices=[('A', 'A - IPv4 Address')])
    alias = RadioField(_('Alias'), [validators.DataRequired()],
        choices=[('Y', 'Yes'), ('N', 'No')])
    ttl = StringField(_('TTL'))
    value = SelectMultipleField(_('IP Addresses'))

class DomainForm(ExtendedForm):
    profile_id = SelectField(_('Profile'), coerce=int)
    ip_id = SelectField(_('IP Addresses'), coerce=int)
    domain = StringField(_('Domain'), [
        validators.DataRequired(),
        validators.Length(min=4, max=64),
        validators.Regexp(domain_re, message=_('invalid domain'))])

class YesNoForm(ExtendedForm):
    yesno = SelectField(_('Yes or No'), [
        validators.DataRequired(),
        validators.AnyOf(['Y'], message='Must Select Yes')],
        choices=[('N', 'No'), ('Y', 'Yes')])

class ProfileForm(ExtendedForm):
    profile = StringField(_('Profile'), [
        validators.DataRequired(), validators.Length(min=4, max=25)])
    note = StringField(_('Note'))

class ProfileRecordForm(ExtendedForm):
    record_type = SelectField(_('Record Type'), [validators.DataRequired()],
        choices=[('A', 'A'), ('MX', 'MX'), ('SPF', 'SPF'), ('TXT', 'TXT')])
    name = StringField(_('Hostname'))
    contents = StringField(_('Contents'), [
        validators.DataRequired(), validators.Length(min=4, max=25)])
