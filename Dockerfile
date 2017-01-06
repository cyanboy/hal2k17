FROM python:3.6-alpine 

ADD bot.py /
ADD requirements.txt /

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "./bot.py" ]