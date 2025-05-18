import paho.mqtt.client as mqtt
import json
import time
import threading
import subprocess  


MQTT_BROKER = "eu1.cloud.thethings.network"  # TODO change for prod
MQTT_TOPIC = "v3/sae-501@ttn/devices/tracker-rom/up"  # TODO set the topic
MQTT_ID = "sae-501@ttn"  # TODO set the client ID
MQTT_API_KEY = "NNSXS.A4B2SMXQHJ242YTXZRNDJG3R24PN5K2OJQIFYIY.45OSGPSAWVRB22ERNZEWJAI2Z5FH4TV3L7TG3743WCSXY2M4KQ2Q"  # TODO set the API key
MQTT_PORT = 1883




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

        url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Click the link to see the map: {url}")

        # Open Firefox with the URL
        subprocess.run(["firefox", url], check=False)  # check=False to avoid crashes if Firefox is not found

    except Exception as e:
        print("\033[91mMQTT Error:\033[0m", e)


def mqtt_receiver():
    """Thread function for receiving messages from the primary broker."""
    client = mqtt.Client(client_id=MQTT_ID, protocol=mqtt.MQTTv311)
    client.username_pw_set(username=MQTT_ID, password=MQTT_API_KEY)
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