FROM python:3.12-alpine

ARG APP_PATH=/opt

WORKDIR $APP_PATH

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

#COPY ./app $APP_PATH/app/req.txt
COPY ./req.txt $APP_PATH/app/req.txt


RUN apk add build-base && \
    pip install --no-cache-dir --upgrade -r $APP_PATH/app/req.txt
