FROM python:3.7-alpine3.7

ARG PORT

ENV FLASK_PORT=${PORT}
ENV FLASK_VERSION=1.0.2

RUN pip install flask==${FLASK_VERSION}

ADD app.py /opt/server/app.py
ENTRYPOINT python /opt/server/app.py
