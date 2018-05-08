FROM ubuntu:16.04


MAINTAINER Gabriele Nocchi <gnocchi@biobam.com>


# Updating package repository
RUN apt-get update


# Dependencies
RUN apt-get install -y sed g++ rsync python perl zip unzip gzip


ADD ./files/app/ /app/


ENV BATCH_CPU=8
ENV BATCH_MEMORY=16000
