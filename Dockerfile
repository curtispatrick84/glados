FROM python:3.6-slim
ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir /GLaDOS
WORKDIR /GLaDOS

COPY requirements.txt /GLaDOS/requirements.txt

RUN pip install -r requirements.txt --pre

COPY . /GLaDOS

EXPOSE 8080
CMD ['/usr/bin/python', '-u', 'server.py']
