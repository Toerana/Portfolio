import paho.mqtt.client as mqtt
import json
import time
import threading
from queue import Queue


MQTT_BROKER = "eu1.cloud.thethings.network"  # TODO change for prod
MQTT_TOPIC = "v3/sae-501@ttn/devices/tracker-rom/up"  # TODO set the topic
MQTT_ID = "sae-501@ttn"  # TODO set the client ID
MQTT_API_KEY = "NNSXS.A4B2SMXQHJ242YTXZRNDJG3R24PN5K2OJQIFYIY.45OSGPSAWVRB22ERNZEWJAI2Z5FH4TV3L7TG3743WCSXY2M4KQ2Q"  # TODO set the API key
MQTT_PORT = 1883


ALTERNATIVE_MQTT_BROKER = "test.mosquitto.org"
ALTERNATIVE_MQTT_PORT = 1883
ALTERNATIVE_MQTT_TOPIC = "gps/coordinates"


alternative_client = mqtt.Client()


message_queue = Queue()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    try:
        
        data = json.loads(msg.payload.decode())
        latitude = data['uplink_message']['decoded_payload']['latitude']
        longitude = data['uplink_message']['decoded_payload']['longitude']
        lat_alt = data['uplink_message']['locations']['frm-payload']['latitude']
        lng_alt = data['uplink_message']['locations']['frm-payload']['longitude']
        
        
        print(f"Latitude: \033[94m{latitude}\033[0m, Longitude: \033[94m{longitude}\033[0m")
        print(f"Alternative Latitude: \033[94m{lat_alt}\033[0m, Longitude: \033[94m{lng_alt}\033[0m")
        print(f"Received at {time.strftime('%H:%M')}")

        
        message_queue.put({"lat": latitude, "lng": longitude})
    
    except Exception as e:
        print("\033[91mMQTT Error:\033[0m", e)

def mqtt_receiver():
    client = mqtt.Client(client_id=MQTT_ID, protocol=mqtt.MQTTv311)
    client.username_pw_set(username=MQTT_ID, password=MQTT_API_KEY)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
    except Exception as e:
        print("MQTT Connection Error:", e)


def mqtt_publisher():
    alternative_client = mqtt.Client()
    alternative_client.connect(ALTERNATIVE_MQTT_BROKER, ALTERNATIVE_MQTT_PORT, 60)
    alternative_client.loop_start()

    while True:
        message = message_queue.get()  
        print("##debug##\n", message,"\n##debug##")
        message = json.dumps(message)  
        alternative_client.publish(ALTERNATIVE_MQTT_TOPIC, message)



def start_mqtt_translator():
    
    receiver_thread = threading.Thread(target=mqtt_receiver, daemon=True)
    publisher_thread = threading.Thread(target=mqtt_publisher, daemon=True)

    receiver_thread.start()
    publisher_thread.start()

