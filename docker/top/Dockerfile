FROM python:3.11.3-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./top /app/top
ADD ./docker /app/docker

RUN chmod +x /app/docker/top/server-entrypoint.sh
RUN chmod +x /app/docker/top/worker-entrypoint.sh
