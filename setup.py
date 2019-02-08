from setuptools import setup

setup(
  name='shelve_it_cli',
  version='0.1',
  description='Python module for assigning containers to locations in ArchivesSpace',
  url='http://github.com/lyrasis/shelve_it_cli',
  author='Mark Cooper',
  author_email='mark.cooper@lyrasis.org',
  license='MIT',
  packages=['shelve_it_cli'],
  zip_safe=False,
  scripts=['bin/shelve_it_cli'],
)
