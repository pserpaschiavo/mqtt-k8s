FROM python:3.10.14-alpine3.19

EXPOSE 1883

WORKDIR /publisher

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mqtt_pub.py .

CMD [ "python", "mqtt_pub.py" ]