from django.shortcuts import redirect
import paho.mqtt.client as mqtt

# MQTT_BROKER = "test.mosquitto.org"  
# MQTT_PORT = 1883
# MQTT_TOPIC = "gps/coordinates/stop"


# def send_shutdown_command():
#     try:
#         for i in range(5):
#             client = mqtt.Client()
#             client.connect(MQTT_BROKER, MQTT_PORT, 60)
#             message = "STOP"
#             client.publish(MQTT_TOPIC, message)
#             print(f"Sent: {message} {i+1} times")
#             time.sleep(1)

#     except Exception as e:
#         print(f"MQTT Error: {e}")



from django.shortcuts import redirect
import paho.mqtt.client as mqtt
import time
import json

MQTT_BROKER = "eu1.cloud.thethings.network"
MQTT_TOPIC = "v3/sae-501@ttn/devices/tracker-rom/down/push" 
MQTT_ID = "" 
MQTT_API_KEY = "NNSXS.A4B2SMXQHJ242YTXZRNDJG3R24PN5K2OJQIFYIY.45OSGPSAWVRB22ERNZEWJAI2Z5FH4TV3L7TG3743WCSXY2M4KQ2Q"
MQTT_PORT = 8883 

def send_shutdown_command():
    try:
        client = mqtt.Client(client_id="", protocol=mqtt.MQTTv311)
        client.username_pw_set(username="sae-501@ttn", password=MQTT_API_KEY)

        client.tls_set()

        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        message = json.dumps({
            "downlinks": [
                {
                    "f_port": 69,  
                    "frm_payload": "1111",  
                    "priority": "HIGH"
                }
            ]
        })
        
        result = client.publish(MQTT_TOPIC, message)
        
        if result[0] == mqtt.MQTT_ERR_SUCCESS:
            print(f"Message sent successfully: {message}")
        else:
            print("Failed to send message")

        client.disconnect()

    except Exception as e:
        print(f"MQTT Error: {e}")

def shutdown_view(request):
    send_shutdown_command()
    return redirect('/')  
