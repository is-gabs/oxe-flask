FROM python:3.7

WORKDIR /app

ADD ./ ./

RUN pip install -r requirements.txt

CMD gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app