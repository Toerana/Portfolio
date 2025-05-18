import paho.mqtt.client as mqtt
import random
import time
import json


MQTT_BROKER = "test.mosquitto.org"  
MQTT_PORT = 1883
MQTT_TOPIC = "gps/coordinates"

LAT_MIN, LAT_MAX = 48.0517, 48.1202  
LNG_MIN, LNG_MAX = 7.3050, 7.4230    


client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def generate_random_coordinates():
    lat = round(random.uniform(LAT_MIN, LAT_MAX), 6)
    lng = round(random.uniform(LNG_MIN, LNG_MAX), 6)
    return {"lat": lat, "lng": lng}

try:
    while True:
        coordinates = generate_random_coordinates()
        payload = json.dumps(coordinates)  
        
        
        client.publish(MQTT_TOPIC, payload)
        print(f"Sent: {payload}")

        time.sleep(20)  

except KeyboardInterrupt:
    print("\nStopping MQTT publisher...")
    client.disconnect()
