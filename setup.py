import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikPyMoPa',

    version='0.1.0',

    description="""Find a Python module's file paths. Have considered Implicit Namespace Packages introduced in PEP 420. Handy for debugging tricky importing problems.""",
    
    long_description="""`Documentation on Github 
<https://github.com/AoiKuiyuyou/AoikPyMoPa/>`_""",

    url='https://github.com/AoiKuiyuyou/AoikPyMoPa',

    author='Aoi.Kuiyuyou',
    
    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='Find Python module file path',

    package_dir = {'':'src'},
    
    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoikpmp=aoikpymopa.aoikpmp:main',
        ],
    },
)
