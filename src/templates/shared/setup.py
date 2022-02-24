from setuptools import setup


setup(name='project-name',
      version='0.0.1',
      license='MIT',
      description='Short description of project-name',
      keywords=['python', 'ansys', 'ace'],
      packages=['project-name'],
      package_dir={'project-name': 'src'},
      install_requires=[],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown'
 )
