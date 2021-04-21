FROM python:2.7-alpine

WORKDIR /app
COPY . /app

RUN apk add --no-cache git make bash
RUN apk add build-base
RUN apk add linux-headers
RUN wget https://github.com/pacparser/pacparser/releases/download/1.3.7/pacparser-1.3.7.tar.gz -O pacparser-1.3.7.tar.gz \
 && sh -c 'tar xvzf pacparser-1.3.7.tar.gz && \
             cd pacparser*/src && \
             make && \
             make install && \
             make pymod && \
             make install-pymod' \
 && rm -rf pacparser*

RUN pip install  -r requirements.txt


CMD [ "uwsgi", "app.ini" ]