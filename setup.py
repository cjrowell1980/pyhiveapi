from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='pyhiveapi',
    version='0.2.17',
    description='A Python library to interface with the Hive API',
    long_description="A Python library to interface with the Hive API",
    url='https://github.com/Rendili/pyhiveapi',

    author='Rendili',
    author_email='rendili@outlook.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
#        'Topic :: Software Development :: API',
        'License :: OSI Approved :: MIT License',
#        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.5.*',
    keywords='Hive API Library',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
#    packages=["pyhiveapi"],
#    install_requires=[],

    entry_points={
        'console_scripts': [
            'pyhiveapi=pyhiveapi.pyhiveapi:Pyhiveapi',
        ],
    }
)
