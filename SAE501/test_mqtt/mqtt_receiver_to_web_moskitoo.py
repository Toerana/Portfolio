import paho.mqtt.client as mqtt
import json
from django.utils.timezone import now
from datetime import timedelta  # Ensure this import is at the top of your script
import subprocess  
import threading



MQTT_BROKER = "test.mosquitto.org"  #TODO change for prod
MQTT_TOPIC = "gps/coordinates/rom"      #TODO set the topic

MQTT_PORT = 1883



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    try:
        print(msg.payload.decode())
        print('############################################')
        data = json.loads(msg.payload.decode())
        print(data)
        lat = data['latitude']
        lng = data['longitude']

       
        url = f"https://www.google.com/maps?q={lat},{lng}"
        print(f"Click the link to see the map: {url}")

        # Open Firefox with the URL
        subprocess.run(["firefox", url], check=False) 
    except Exception as e:
        print("MQTT Error:", e)


def mqtt_receiver():
    """Thread function for receiving messages from the primary broker."""
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
    except Exception as e:
        print("MQTT Connection Error:", e)


def start_mqtt_translator():
    
    receiver_thread = threading.Thread(target=mqtt_receiver, daemon=True)

    receiver_thread.start()

if __name__ == "__main__":
    start_mqtt_translator()
    while True:
        pass