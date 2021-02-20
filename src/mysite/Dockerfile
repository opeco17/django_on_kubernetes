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

ENV PROJECT_NAME mysite
RUN mkdir -p /var/log/${PROJECT_NAME}

WORKDIR ${HOME}/${PROJECT_NAME}
ENV DJANGO_SETTINGS_MODULE config.settings.production

WORKDIR ${HOME}
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]