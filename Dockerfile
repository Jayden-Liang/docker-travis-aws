FROM python:3.6-slim

RUN apt-get update && apt-get install -y gcc
RUN apt-get update && apt-get -y install default-libmysqlclient-dev

ENV INSTALL_PATH /project
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN pip3 install --editable .

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "project.app:create_app()"
