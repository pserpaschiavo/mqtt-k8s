FROM python:3.10.14-alpine3.19

EXPOSE 1883

WORKDIR /subscriber

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY mqtt_sub.py .

CMD [ "python", "mqtt_sub.py" ]