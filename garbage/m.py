import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import time

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("/mrmin/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message


mqttc.connect("levandrovskiy.ru", 1883, 60)
mqttc.loop_start()
while 1:
    mqttc.publish("/mrmin/truck/Rotation-1", "right")
    mqttc.publish("/mrmin/", "right")
    time.sleep(1)
mqttc.loop_stop()
mqttc.disconnect()
