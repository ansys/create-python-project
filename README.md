
<h1 align="center">
  <a href=""><img src="https://raw.githubusercontent.com/pyansys/create-python-project/main/doc/images/create-python-project_transparent.png" alt="Create Python Project"></a>
</h1>

<p align="center">
  <a href="https://pypi.org/project/ansys-create-python-project/"><img src="https://img.shields.io/pypi/v/ansys-create-python-project.svg"></a>
  <a href="https://pypi.org/project/ansys-create-python-project/"><img src="https://img.shields.io/pypi/status/ansys-create-python-project.svg"></a>
  <a href="https://pypi.org/project/ansys-create-python-project/"><img src="https://img.shields.io/pypi/pyversions/ansys-create-python-project.svg"></a>
  <a href="CONTRIBUTING.md#pull-requests"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="#license"><img src="https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg?colorB=ff0000"></a>
</p>

## Quick Overview

Easily create a new Python project with simple commands:

```shell
pipx run ansys-create-python-project -n my-project
```
or

```shell
python -m ansys-create-python-project -n my-project
```

<h1 align="center">
  <a href=""><img src="https://raw.githubusercontent.com/pyansys/create-python-project/main/doc/images/pipx_create_project.gif" alt="Create Python Project"></a>
</h1>

The new python project will be created according to the Ansys-recommended structure.

For example, the commands above will create a directory called `my-project` inside the current directory.<br>

View the full documentation [here](https://pyansys.github.io/create-python-project/index.html).

## Prerequisites

- Python 3.8+
- pip
- pipx (Optional but recommended)

This tool is compatible with Windows OS and Linux distributions.

## Usage

### Create new project 

#### With pipx

```shell
pipx run ansys-create-python-project -n my-project 
```

[pipx](https://pypa.github.io/pipx/) is a package runner tool that that helps to run applications written in Python.
In fact, it uses pip, but is focused on installing and managing Python packages that can be run from the command line 
directly as applications. pipx requires Python 3.6+ and can be installed by following 
[these instructions](https://pypa.github.io/pipx/installation/).

It will create a directory called `my-project` inside the current folder.<br>
Inside that directory, it will generate the initial project structure and install 
the transitive dependencies:

```
my-project
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── flake8
├── pytest.ini
├── requirements.txt
├── package.json
├── CHANGELOG.md
├── .gitignore
├── .gitattributes
├── docker
│   ├── dockerfile
│   └── docker-compose.yml
├── doc
│   ├── images
│   |     └── img.jpeg
│   └── README.md
├── src
│   └── app.py
├── tests
│    └── test_app.py
└── examples
    └── README.md
   
```

No configuration or complicated folder structures required, only the files you need to build your app.<br>


#### With pip

If you do not want to install pipx you can still use the package, but first you must install it with pip.

```shell
pip install ansys-create-python-project
```
Then, you can run the package using Python's `python -m` functionality.

```shell
python -m ansys-create-python-project -n my-project
```

If you aren't sure what sort of arguments you need to supply you can always view the help through the following command.

```shell
python -m ansys-create-python-project --help
```

#### Specify other templates

The default project template is 'classic'. However, there are several other templates available.
You can view the available templates by running the following command.

```shell
pipx run ansys-create-python-project --template
```

You can easily specify other templates with the `-t` flag.

```sh
pipx run ansys-create-python-project -n my-project -t rest-api
```

### Run tests locally

The project newly created is done with a docker and a docker-compose files in the `/tests` folder. That enables to run 
all tests very easily in any environment without any additional requirements (only [docker](https://docs.docker.com/get-docker/) 
and [docker-compose](https://docs.docker.com/compose/install/) are required).

To run the tests run the following command:
1. Move to /tests folder
2. Build the docker image
3. Start a container
4. Run the tests
5. Optional: Run specific tests suites thanks to the powerful pytest search feature

<h1 align="center">
  <a href=""><img src="https://raw.githubusercontent.com/pyansys/create-python-project/main/doc/images/docker-compose-run-tests.gif" alt="Create Python Project"></a>
</h1>

### Push your new project to git repository

1- Go inside the created directory by running 
```sh
cd ./my-project
```

2- Push this project in git remote repository"
```sh
git init

git remote add origin <git_repository_url>

git add . && git commit -m \"initial commit\"

git push origin main

```

