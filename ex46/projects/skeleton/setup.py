try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'descritpion': 'My Project',
    'author': 'Polus',
    'url': 'URL',
    'download_url': ' download URL',
    'author_email': 'aleksandrabacik@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['project'],
    'scripts': ['bin'],
    'name': 'project'
}

setup(**config)
