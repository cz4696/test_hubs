# -*- coding: utf-8 -*-
"""
Time:2022/8/22 18:09
Author:CAOZHENG
File:mqtt_subscribe.py
"""

from paho.mqtt import client as mqtt_client
from config import mqtt_cfg

client = mqtt_client.Client(mqtt_cfg.CLIENT_ID)


def connect_mqtt():
    """连接 mqtt"""

    def on_connect(client, userdata, flags, rc):
        """连接回调函数"""

        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect, return code ", rc)

    client.on_connect = on_connect
    client.username_pw_set(mqtt_cfg.USERNAME, mqtt_cfg.PASSWORD)
    client.connect(mqtt_cfg.HOST, mqtt_cfg.PORT, mqtt_cfg.KEEPALIVE)
    client.loop_start()


def subscribe():
    def on_message(client, userdata, msg):
        """消息接收"""
        # with open('D://msg.proto', 'r+') as file:
        #     file.write("syntax='proto3';\n")
        #     file.write(str(msg.payload.decode('ignore')))
        #     data = file.read()
        #     message, typedef = blackboxprotobuf.protobuf_to_json(data)
        #     print(data)
        #     index = data.find('^')
        #     file.truncate(0)
        #     file.close()
        index_start = str(msg.payload).find('^') + 1
        index_end = str(msg.payload).find("}'") + 1
        message = str(msg.payload)[index_start:index_end]
        print("topic:" + msg.topic + " message:" + message)

    client.subscribe(mqtt_cfg.TOPIC)
    client.on_message = on_message


def run():
    connect_mqtt()
    subscribe()
    while True:
        pass


if __name__ == '__main__':
    run()
