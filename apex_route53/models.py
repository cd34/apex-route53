from sqlalchemy import (Column,
                        ForeignKey,
                        types,
                        Unicode)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (relationship,   
                            scoped_session,
                            sessionmaker)
from sqlalchemy.sql.expression import func

from zope.sqlalchemy import ZopeTransactionExtension

#DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class Registrar(Base):
    __tablename__ = 'registrars'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(types.Integer(), primary_key=True)
    registrar = Column(Unicode(80), default=u'')
    url = Column(Unicode(80), default=u'')
    created = Column(types.DateTime(), default=func.now())

class Provider(Base):
    __tablename__ = 'providers'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(types.Integer(), primary_key=True)
    name = Column(Unicode(80), default=u'')
    url = Column(Unicode(80), default=u'')
    os = Column(types.Integer())
    created = Column(types.DateTime(), default=func.now())

class IP(Base):
    __tablename__ = 'ips'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(types.Integer(), primary_key=True)
    ip_address = Column(Unicode(80), default=u'')
    provider_id = Column(types.Integer(), ForeignKey(Provider.id))
    note = Column(Unicode(80), default=u'')
    created = Column(types.DateTime(), default=func.now())

    provider = relationship('Provider', uselist=False)

class Profile(Base):
    __tablename__ = 'profiles'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(types.Integer(), primary_key=True)
    profile = Column(Unicode(80), default=u'')
    note = Column(Unicode(80), default=u'')
    created = Column(types.DateTime(), default=func.now())

class Profile_Record(Base):
    __tablename__ = 'profile_records'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(types.Integer(), primary_key=True)
    profile_id = Column(types.Integer(), ForeignKey(Profile.id))
    name = Column(Unicode(80), default=u'')
    record_type = Column(Unicode(80), default=u'')
    contents = Column(Unicode(80), default=u'')
    created = Column(types.DateTime(), default=func.now())

def initialize_sql(engine, settings):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate(settings)
    except IntegrityError:
        pass

def populate(settings):
    session = DBSession()
