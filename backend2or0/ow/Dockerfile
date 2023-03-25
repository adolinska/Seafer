FROM python:alpine3.17

RUN apk add --no-cache tzdata
ENV TZ=Europe/Warsaw

RUN mkdir /pcss
WORKDIR /pcss

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /pcss
COPY database.py /pcss
COPY misc.py /pcss
COPY static /pcss/static
COPY templates /pcss/templates

ENV FLASK_APP=app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
