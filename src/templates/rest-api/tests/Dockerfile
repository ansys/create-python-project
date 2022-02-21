FROM python:3.8-buster
MAINTAINER ansys_developer

RUN mkdir /pytest_project/
COPY ../test-requirements.txt /pytest_project/
RUN pip install --upgrade pip
RUN pip3 install -r /pytest_project/requirements_test.txt

WORKDIR /pytest_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
