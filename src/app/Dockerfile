FROM python:3.8.0

ENV HOME /home/workspace
RUN mkdir ${HOME}
WORKDIR ${HOME}

COPY requirements.txt ${HOME}

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y vim && \
  pip install -r requirements.txt

COPY . ${HOME}

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]