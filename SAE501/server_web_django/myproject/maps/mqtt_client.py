import paho.mqtt.client as mqtt
import json
from django.utils.timezone import now
from maps.models import Coordinate
from datetime import timedelta  # Ensure this import is at the top of your script



MQTT_BROKER = "test.mosquitto.org"  #TODO change for prod
MQTT_TOPIC = "gps/coordinates"      #TODO set the topic

def on_message(client, userdata, msg):
    try:
        print(f"Message received : {msg.payload.decode()}")
        payload = json.loads(msg.payload.decode()) 
        lat, lng = payload["lat"], payload["lng"]
        timedelta_is = now() - timedelta(seconds=2)
        if Coordinate.objects.filter(latitude=lat, longitude=lng, timestamp__range=(timedelta_is, now())).exists():
            print(f"Coordinate already exists within the last 10 seconds: {lat}, {lng}")
        else:
            Coordinate.objects.create(latitude=lat, longitude=lng, timestamp=now())
            print(f"New coordinate saved: {lat}, {lng}")
    except Exception as e:
        print("MQTT Error:", e)

def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60) 
    client.subscribe(MQTT_TOPIC)     
    print("connected to mqtt")     
    client.loop_start()

# MQTT_BROKER = "eu1.cloud.thethings.network"  # TODO change for prod
# MQTT_TOPIC = "v3/sae-501@ttn/devices/tracker-rom/up"  # TODO set the topic
# MQTT_ID = "sae-501@ttn"  # TODO set the client ID
# MQTT_API_KEY = "NNSXS.A4B2SMXQHJ242YTXZRNDJG3R24PN5K2OJQIFYIY.45OSGPSAWVRB22ERNZEWJAI2Z5FH4TV3L7TG3743WCSXY2M4KQ2Q"  # TODO set the API key
# MQTT_PORT = 1883


# def on_message(client, userdata, msg):
#     print("Message received")
#     try:
        
#         payload = json.loads(msg.payload.decode())  # Expecting structured JSON
#         print("Payload:", payload)
#         # Primary coordinates
#         lat = payload['uplink_message']['decoded_payload']['latitude']
#         lng = payload['uplink_message']['decoded_payload']['longitude']
#         # Alternative coordinates
#         lat_alt = payload['uplink_message']['locations']['frm-payload']['latitude']
#         lng_alt = payload['uplink_message']['locations']['frm-payload']['longitude']

#         print(f"Latitude: {lat}, Longitude: {lng}")
#         print(f"Alternative Latitude: {lat_alt}, Longitude: {lng_alt}")

#         # Save the primary coordinates to the database
#         Coordinate.objects.create(latitude=lat, longitude=lng, timestamp=now())
#         print(f"New coordinate saved: {lat}, {lng}")
#     except Exception as e:
#         print("YEEEEEEET")
#         print("MQTT Error:", e)

# def start_mqtt():
#     print("Connecting to MQTT Broker...")

#     client = mqtt.Client(client_id=MQTT_ID, protocol=mqtt.MQTTv311)
#     client.username_pw_set(username=MQTT_ID, password=MQTT_API_KEY)
#     print("connected ?")
#     client.on_message = on_message


