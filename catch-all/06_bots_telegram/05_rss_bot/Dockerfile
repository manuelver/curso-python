FROM python:3.10-alpine

WORKDIR /app

COPY . /app/

RUN apk update && apk upgrade && \
    apk add sqlite sqlite-libs sqlite-dev && \
    pip install -r requirements.txt

CMD ["python", "rss2telegram.py"]
