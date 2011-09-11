from setuptools import setup, find_packages
 
version = '0.0.1'

setup(
    name = 'marmaladed',
    version = version,
    description = "marmaladed is a simple django memcached console",
    classifiers = [
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords = 'memcached,django',
    author = 'Giovanni Ferron',
    author_email = 'info@gvnn.it',
    url = 'http://github.com/gvnn/marmaladed/tree/master',
    license = 'Apache License, Version 2.0',
    packages = find_packages(),
    zip_safe = False,
    install_requires = ['setuptools'],
    include_package_data = True,
    setup_requires = ['setuptools_git'],
)