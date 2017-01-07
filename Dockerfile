FROM resin/rpi-raspbian
FROM python:3.6

RUN mkdir /app
ADD requirements.txt /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "./bot.py" ]