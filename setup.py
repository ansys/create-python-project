from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]

setup(name='ansys-create-python-project',
      version='0.0.5',
      url='',
      author='ANSYS, Inc.',
      maintainer='Babacar Fall',
      maintainer_email='babacar.fall@ansys.com',
      license='MIT',
      entry_points={"console_scripts": ["ansys-create-python-project = src.main:cli"]},
      description='Ansys Python Project Creator',
      keywords=['python', 'ansys', 'ace'],
      packages=find_packages(),
      install_requires=['easygui', 'coloredlogs', 'emoji','humanfriendly','pyreadline3'],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      include_package_data=True,
      package_data={'src.templates': ['../*']},
      zip_safe=False,
      classifiers=CLASSIFIERS,
 )