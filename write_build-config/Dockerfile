FROM python:3-slim-bookworm

WORKDIR /usr/src/build-config-updater

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY build-config-updater.py .

CMD ["python", "build-config-updater.py"]