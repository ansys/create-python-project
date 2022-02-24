from setuptools import setup


setup(name='$project_name',
      version='0.0.1',
      license='MIT',
      description='Short description of $project_name',
      keywords=['python', 'ansys', 'ace'],
      packages=['$project_name'],
      package_dir={'$project_name': 'src'},
      install_requires=[],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown'
 )
