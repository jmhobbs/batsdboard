from setuptools import setup


setup(
    name='batsdboard',
    version='0.0.1',
    url='https://github.com/jmhobbs/batsdboard',
    license='MIT',
    author='John Hobbs',
    author_email='john@velvetcache.org',
    description='batsdboard is a Flask embeddable dashboard for batsd.',
    long_description=__doc__,
    package_dir={'': 'src'},
    packages=['batsdboard'],
    scripts=['src/batsdboard_server.py'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring',
    ]
)
