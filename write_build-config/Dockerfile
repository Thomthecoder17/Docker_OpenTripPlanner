FROM python:3.11-slim

RUN apt-get update

WORKDIR /build-config-updater

COPY build-config-updater.py 

CMD ["python", "build-config-updater.py"]