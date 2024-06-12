FROM python:3.10.14-alpine3.19

EXPOSE 1883

WORKDIR /subscriber

RUN pip install paho-mqtt==1.6.0

COPY mqtt_sub.py .

CMD [ "python", "mqtt_sub.py" ]