FROM python:3.10.14-alpine3.19

EXPOSE 1883

WORKDIR /publisher

RUN pip install paho-mqtt==1.6.0

COPY mqtt_pub.py .
COPY config-pub.sh .

CMD [ "sh" ]
