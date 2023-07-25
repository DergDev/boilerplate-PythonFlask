FROM python:3.9-slim-buster
RUN mkdir -p /app/logs
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod 755 ./gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]

EXPOSE 5000
