import json
import os
from pathlib import Path

import mysql.connector
import paho.mqtt.client as mqtt
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        for topic in settings.MQTT_TOPICS:
            mqtt_client.subscribe(topic)
    else:
        raise ('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    if 'sinewave' in msg.topic:
        message = json.loads(msg.payload)
        data = message['data']
        timestamp = message['Time']
        freq = len(data)
        noise_sinewave(data, timestamp, freq)
    elif 'heartbeat' in msg.topic:
        message = json.loads(msg.payload)
        data = message['data']
        timestamp = message['Time']
        freq = message['freq']
        noise_heartbeat(data, timestamp, freq)


def noise_sinewave(dataset: float, timestamp, freq: int):
    cnx = mysql.connector.connect(read_default_file=str(os.path.join(BASE_DIR, 'configs', 'my.cnf')))
    cur = cnx.cursor()
    time_const = 1 / freq
    data = []
    for i in range(len(dataset)):
        data.append((dataset[i], timestamp + (time_const * i)))
    cur.executemany('insert into dashboard_sinedata (data_val, label) values'
                    ' (%s,from_unixtime(%s));', data)
    cnx.commit()
    cnx.close()


def noise_heartbeat(dataset: float, timestamp, freq: int):
    cnx = mysql.connector.connect(read_default_file=str(os.path.join(BASE_DIR, 'configs', 'my.cnf')))
    cur = cnx.cursor()
    time_const = freq / 3600
    data = []
    for i in range(len(dataset)):
        data.append((dataset[i], timestamp + (time_const * i)))
    cur.executemany('insert into dashboard_heartbeatdata (`value`, time_stamp) values'
                    ' (%s,from_unixtime(%s));', data)
    cnx.commit()
    cnx.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
