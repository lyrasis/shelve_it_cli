from setuptools import setup

setup(
    name='shelve_it_cli',
    version='0.1',
    description='Assigning containers to locations in ArchivesSpace',
    url='https://github.com/lyrasis/shelve_it_cli',
    author='Mark Cooper',
    author_email='mark.cooper@lyrasis.org',
    license='MIT',
    packages=['shelve_it_cli'],
    install_requires=[
        'ArchivesSnake==0.7.3',
        'fire==0.1.3',
    ],
    scripts=['bin/shelve_it_cli'],
    zip_safe=False
)
