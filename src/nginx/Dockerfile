FROM nginx:1.13

ENV ENTRYKIT_VERSION 0.4.0

RUN apt-get update \
  && apt-get install -y wget \
  && wget https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
  && tar -xvzf entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
  && rm entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
  && mv entrykit /usr/local/bin/ \
  && entrykit --symlink

COPY nginx.conf.tmpl /etc/nginx/

ENV PROJECT_NAME mysite

RUN mkdir -p /var/www/${PROJECT_NAME}/static
RUN mkdir -p /var/www/${PROJECT_NAME}/media

COPY static /var/www/${PROJECT_NAME}/static
COPY media /var/www/${PROJECT_NAME}/media

ENTRYPOINT ["render", "/etc/nginx/nginx.conf", "--"]

CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
