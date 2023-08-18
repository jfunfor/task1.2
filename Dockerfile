FROM python:3.10-alpine
COPY . /opt/kv-storage/
WORKDIR /opt/kv-storage
RUN apk update && pip3 install --upgrade pip && pip3 install -r requirements.txt
CMD python3 manage.py

EXPOSE 5000