try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'descritpion': 'Exercise 47',
    'author': 'Polus',
    'url': 'URL',
    'download_url': ' download URL',
    'author_email': 'aleksandrabacik@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
