import paho.mqtt.client as mqtt
import time


class Mqtt:
    def __init__(self, host, port):
        self.client = mqtt.Client()

        self.client.on_connect = self.onConnect
        self.client.on_message = self.onMessage

        self.client.connect(host, port)
        self.client.subscribe('TEST')

        self.client.loop_start()

        pass

    def onConnect(self, client, userdata, flag, rc):
        print('Connected to broker...')
        pass

    def onMessage(self, client, userdata, packet):
        topic = packet.topic
        msg = packet.payload.decode('utf-8')
        print(f'{topic}: {msg}')

    def publish(self, topic, payload):
        self.client.publish(topic, payload)


connection = Mqtt('localhost', 1883)

while True:
    connection.publish('Topic', 'This is payload from python.')
    time.sleep(5)
    pass
