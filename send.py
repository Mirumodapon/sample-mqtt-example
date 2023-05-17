import paho.mqtt.publish as publish
import json

host = '163.24.242.176'
port = 8333
#auth = { 'username': 'test', 'password': '123456' }
topic = 'test'
payload = {'key1':'value1', 'key2':'value2'}
payload = json.dumps(payload)
publish.single(topic, payload, hostname=host, port=port)
#publish.single(topic, payload, hostname=host, port=port, auth=auth)
