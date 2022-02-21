FROM python:3.8-buster
MAINTAINER ansys_developer

RUN mkdir /pytest_project/
COPY ../requirements_test.txt /pytest_project/
COPY ../setup.py ./setup.py
COPY ../README.md ./README.md

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /pytest_project/requirements_test.txt

WORKDIR /pytest_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
