import os.path
from setuptools import setup, find_packages

_URI = 'https://github.com/neuront/pyunicodeblock'

setup(
    name='unicodeblock',
    version='0.3.0',
    author='Neuron Teckid',
    author_email='lene13@gmail.com',
    license='MIT',
    keywords='Python UnicodeBlock',
    url=_URI,
    description='Python Unicode Block Utilities',
    packages=['unicodeblock'],
    long_description='Visit ' + _URI + ' for details please.',
    install_requires=[],
    zip_safe=False,
)
