from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()


setup(
    name='indigo-gm',
    version=version,
    description='Indigo platform plugin for integrating with Gazette Machine',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/laws-africa/indigo-gm',

    # Author details
    author='Laws.Africa',
    author_email='greg@laws.africa',

    # See https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['docs']),
    include_package_data=True,

    python_requires='~=3.6',
    install_requires=[
        'indigo>=3',
        'requests>=2',
    ],
)
