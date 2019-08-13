# installation: pip install binary_heap

from setuptools import setup


setup(
    name='binary_heap',
    version='1.0.4',
    description='Python functions for working with Binary Heap',
    keywords='binary-heap heap python-heap min-heap max-heap heap-sort',
    long_description=open('README.rst').read(),

    author='Ramesh RV',
    author_email='rameshrvr@outlook.com',
    url='https://github.com/rameshrvr/binary_heap',

    platforms=['All'],
    license='GNU General Public License v3.0',

    packages=['binary_heap'],

    classifiers=[
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
