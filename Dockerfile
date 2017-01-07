FROM resin/rpi-raspbian

RUN mkdir /app
ADD requirements.txt /app

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3
RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "./bot.py" ]