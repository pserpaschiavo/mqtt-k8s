import random
import string
import time
import os

from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io'
broker = os.environ["CLUSTER_IP"]
port = int(os.environ["CLUSTER_PORT"])
topic = "ufes/nerds"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

msg_max = int(os.environ["MSG_MAX"])
msg_length = int(os.environ["MSG_LENGTH"])
msg_time = int(os.environ["MSG_TIME"]) / 1000

def get_message(length):
    msg = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return msg

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    while True:
        time.sleep(msg_time)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > msg_max:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    # client.loop_forever()


if __name__ == '__main__':
    run()
