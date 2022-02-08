.. _Examples:

Examples
========

Python projects can be created using this tool in two ways:
via pip and with pipx.

If you use pipx you don't have to install the package itself,
but you do have to install pipx. Whereas if you use pip you
must install the package via pip (as normal) and run the package
from there. Examples of both will be used in the examples but
whilst the syntax may differ slightly between pip and pipx the
functionality is the same.

Classic template (default)
--------------------------

The ``classic`` template is the default in the tool, and will be used if no template is specified.

The minimum you need to provide is the name of your project using either the ``--Name`` or ``-n`` flags.

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project -n my_project
    12:57:50 [INFO] Project created successfully
    We recommend you track your project using git
    and store it in a remote repository, such as on ADO or GitHub.
    This can be done by following these instructions provided you already have git installed.
        1- Navigate to the created project directory on the command line
        2- Make the directory into a git repo and link it to a remote origin (GitHub/ADO/etc.)
            2.1 [Optional] -  git init
            2.2 [Optional] -  git remote add origin <git_repository_url>
            2.3 [Optional] -  git add . && git commit -m "initial commit"
            2.4 [Optional] -  git push origin main


    PS C:\>
    PS C:\> cd .\my_project\
    PS C:\> ls


        Directory: C:\my_project


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----        04/02/2022     17:49                doc
    d-----        04/02/2022     17:49                docker
    d-----        04/02/2022     17:49                examples
    d-----        04/02/2022     17:49                src
    d-----        04/02/2022     17:49                tests
    -a----        04/02/2022     17:49            281 .flake8
    -a----        04/02/2022     17:49            240 .gitattributes
    -a----        04/02/2022     17:49            998 .gitignore
    -a----        04/02/2022     17:49             11 CHANGELOG.md
    -a----        04/02/2022     17:49           2750 CODE_OF_CONDUCT.md
    -a----        04/02/2022     17:49             41 conftest.py
    -a----        04/02/2022     17:49           2879 CONTRIBUTING.md
    -a----        04/02/2022     17:49           1110 LICENSE
    -a----        04/02/2022     17:49            200 pytest.ini
    -a----        04/02/2022     17:49            110 README.md
    -a----        04/02/2022     17:49             35 requirements.txt
    -a----        04/02/2022     17:49            389 setup.py
    -a----        04/02/2022     17:49            109 test-requirements.txt


View available templates
------------------------

Create-Python-Package comes with several builtin templates, which can be viewed in detail on
the :ref:`Templates`. page. If you want to view those available to you you can also use the
``--templates`` flag to interrogate the CLI.

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project --templates
    Available templates are:
     * classic
     * gRPC-api
     * package
     * rest-api


Version number
--------------

Similarly you can interrogate the version number of the version you're using via the ``--version`` flag.

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project --version
    ansys-create-python-project 0.0.2dev


Creating a project whilst specifying a template
-----------------------------------------------

In order to specify a template you must use the ``--Template`` (or ``-t``) flag.
For example, to create a new package called "my_package", you would need to execute the following command.

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project -n my_package -t package
    11:56:59 [INFO] Project created successfully
    We recommend you track your project using git
    and store it in a remote repository, such as on ADO or GitHub.
    This can be done by following these instructions provided you already have git installed.
        1- Navigate to the created project directory on the command line
        2- Make the directory into a git repo and link it to a remote origin (GitHub/ADO/etc.)
            2.1 [Optional] -  git init
            2.2 [Optional] -  git remote add origin <git_repository_url>
            2.3 [Optional] -  git add . && git commit -m "initial commit"
            2.4 [Optional] -  git push origin main


    PS C:\>

Viewing the help
----------------

If you're still having trouble understanding the command line, you can always view the help using the
``--help`` or ``-h`` flags.

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project -h
    usage: __main__.py [-h] [-n NAME] [-t TEMPLATE] [--templates] [--version]

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --Name NAME  Set the project name. This is a required argument.
      -t TEMPLATE, --Template TEMPLATE
                            Set the project template. Defaults to 'classic'.
      --templates           View all the available project templates.
      --version             show program's version number and exit

or

.. code-block:: powershell

    PS C:\> python -m ansys-create-python-project --help
    usage: __main__.py [-h] [-n NAME] [-t TEMPLATE] [--templates] [--version]

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --Name NAME  Set the project name. This is a required argument.
      -t TEMPLATE, --Template TEMPLATE
                            Set the project template. Defaults to 'classic'.
      --templates           View all the available project templates.
      --version             show program's version number and exit

