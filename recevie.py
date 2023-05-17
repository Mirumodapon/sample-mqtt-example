import paho.mqtt.client as mqtt
import json

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

# 設定 MQTT 代理的資訊
broker_address = "163.24.242.176"
broker_port = 8333
#username = "test"
#password = "123456"

# 建立 MQTT 用戶端
client = mqtt.Client()

# 設定用戶名和密碼
#client.username_pw_set(username, password)

# 連線到 MQTT 代理
client.connect(broker_address, broker_port)

# 訂閱主題
topic = "test"
client.subscribe(topic)

# 定義訊息接收的回調函數
def on_message(client, userdata, message):
    json_message = json.loads(str(message.payload.decode("utf-8")))
    print("Received message:", json_message)
    #water = int(json_message)
    #while True:
        #GPIO.output(18,GPIO.HIGH)
        #print('ON')
        #for i in range(water):
            #print(i+1,'second')
            #sleep(1)
        #GPIO.output(18,GPIO.LOW)
        #print ('OFF')
        #break

# 設定訊息接收的回調函數
client.on_message = on_message

# 開始接收訊息
client.loop_forever()
