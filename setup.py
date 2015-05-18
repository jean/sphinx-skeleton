# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the skeleton Sphinx extension.

.. add description here ..
'''

requires = ['Sphinx>=0.6', 'monkey']

setup(
    name='sphinxcontrib-skeleton',
    version='0.1',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-skeleton',
    license='BSD',
    author='Jean Jordaan',
    author_email='jean.jordaan@gmail.com',
    description='Sphinx "skeleton" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Sphinx :: Extension',
        #'Framework :: Sphinx :: Theme',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
