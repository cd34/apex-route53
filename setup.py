import os

from setuptools import find_packages
from setuptools import setup

version = '0.9.10'

install_requires = [
    "zope.sqlalchemy",
    "pyramid>1.1.2",
    "apex",
    "route53",
]

tests_require = install_requires + ['Sphinx', 'docutils',
                                    'WebTest', 'virtualenv',
                                    'nose', 'coverage']

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGELOG.txt')) as f:
        CHANGELOG = f.read()
except IOError:
    README = CHANGELOG = ''

kwargs = dict(
    version=version,
    name='apex_route53',
    description="Pyramid toolkit for managing AWS Route53 DNS zones",
    long_description=README + '\n\n' + CHANGELOG,
    classifiers=[
      "Intended Audience :: Developers",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
    ],
    install_requires=install_requires,
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    tests_require=tests_require,
    test_suite="apex_route53.tests",
    url="http://thesoftwarestudio.com/apex_route53/",
    author="Chris Davies",
    author_email='user@domain.com',
    entry_points="""\
        [paste.paster_create_template]
        apex_routesalchemy=apex.scaffolds:ApexRoutesAlchemyTemplate
    """
)

try:
    import babel
    babel = babel  # PyFlakes
    kwargs['message_extractors'] = {".": [
        ("**.py",     "lingua_python", None),
        ('**.mako', 'mako', None),
        ("**.pt", "lingua_xml", None), ]
    }
except ImportError:
    pass

setup(**kwargs)
