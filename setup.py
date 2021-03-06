"""
packaging setup for ainawuffa
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
#from codecs import open
import os
import sys
import versioneer

here = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(here, 'ainawuffa', ))
import ainawuffa as package

__entry_points__  = {
    'console_scripts': [
        'ainawuffa_toot = ainawuffa.main:toot',
        ],
    #'gui_scripts': [],
}

setup(
    author           = package.__author__,
    author_email     = package.__author_email__,
    classifiers      = package.__classifiers__,
    description      = package.__description__,
    entry_points     = __entry_points__,
    license          = package.__license__,
    long_description = package.__long_description__,
    install_requires = package.__install_requires__,
    name             = package.__project__,
    #platforms        = package.__platforms__,
    packages         = find_packages(exclude=[
        #'docs', 
        #'examples', 'tests'
        ]),
    url              = package.__url__,
    version          = versioneer.get_version(),
    cmdclass         = versioneer.get_cmdclass(),
    zip_safe         = package.__zip_safe__,
    python_requires  = '>=3.5',
 )
