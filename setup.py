from setuptools import setup, find_packages
import sys, os

version = '0.1RC'

setup(
    name='ckanext-glasgow_theme',
    version=version,
    description="Glasgow's Theme for CKAN",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Devon Walshe / Marek Bell',
    author_email='devon.walshe@gmail.com',
    url='data.glasgow.gov.uk',
    license='OGL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.glasgow_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        glasgow_theme=ckanext.glasgow_theme.plugin:GlasgowThemePlugin
    ''',
)
