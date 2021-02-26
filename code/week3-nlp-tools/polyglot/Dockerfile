FROM continuumio/anaconda3

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev vim --no-install-recommends

COPY ./ ./app
WORKDIR ./app

RUN pip install -r requirements.txt
