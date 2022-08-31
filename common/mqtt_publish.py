# -*- coding: utf-8 -*-
"""
Time:2022/8/22 18:06
Author:CAOZHENG
File:mqtt_publish.py
"""

import time
from paho.mqtt import client as mqtt_client
from config import mqtt_cfg


def connect_mqtt():
    """连接 mqtt服务器"""

    def on_connect(client, userdata, flags, rc):
        """连接回调函数"""

        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect, return code ", rc)

    # 连接mqtt代理服务器，并获取连接引用
    client = mqtt_client.Client(mqtt_cfg.CLIENT_ID)
    client.on_connect = on_connect
    client.connect(mqtt_cfg.HOST, mqtt_cfg.PORT, mqtt_cfg.KEEPALIVE)
    client.username_pw_set(username=mqtt_cfg.USERNAME, password=mqtt_cfg.PASSWORD)
    return client


def publish(client):
    """发布消息"""

    while True:
        # 每隔5秒发布一次信息
        time.sleep(5)
        msg = f'hello'
        result = client.publish(mqtt_cfg.TOPIC, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{mqtt_cfg.TOPIC}`")
        else:
            print(f"Failed to send message to topic {mqtt_cfg.TOPIC}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
