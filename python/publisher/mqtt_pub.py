import random
import string
import time
import os
import argparse

from paho.mqtt import client as mqtt_client

broker = os.environ["CLUSTER_IP"]
port = int(os.environ["CLUSTER_PORT"])
topic = "ufes/nerds"

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--msg-max", type=int, help="Set the maximum mensages for session.")
parser.add_argument("-l", "--msg-length", type=int, help="Set the size of sent messages.")
parser.add_argument("-r", "--msg-time", type=int, help="Set the interval of time for each messages sent (in milisseconds)")

args = parser.parse_args()

msg_max = args.msg_max
msg_length = args.msg_length
msg_time = (args.msg_time) / 1000


# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def get_message(msg_length):
    msg = ''.join(random.choice(string.ascii_letters) for i in range(msg_length))
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
    msg = get_message(msg_length)
    while True:
        time.sleep(msg_time)
        status_msg = f"messages {msg_count}: {msg}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send '{status_msg}' to topic '{topic}'")
        else:
            print(f"Failed to send message to topic '{topic}'")
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
