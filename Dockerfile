FROM alpine:latest

RUN mkdir /app
ADD requirements.txt /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "./bot.py" ]