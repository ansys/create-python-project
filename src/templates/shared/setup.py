from setuptools import setup, find_packages


setup(name='project-name',
      version='0.0.1',
      license='MIT',
      description='Short description of project-name',
      keywords=['python', 'ansys', 'ace'],
      packages=find_packages(),
      install_requires=[],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown'
 )