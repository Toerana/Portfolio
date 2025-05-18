import paho.mqtt.client as mqtt
import random
import time
import json


MQTT_BROKER = "test.mosquitto.org"  
MQTT_PORT = 1883
MQTT_TOPIC = "gps/coordinates"

coordonnees_personne = {"0":"48.078110/7.362396","1": "48.076349/7.363704", "2": "48.075366/7.397441", "3": "48.065613/7.368283", "4": "0.1/0.1"}

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)



try:
    while True:
        person = input("Entrez l'id de la personne (0,1,2,3,4): ")
        if person not in coordonnees_personne:
            print("Personne inconnue")
            continue
        else:
            coordinates = coordonnees_personne[person].split("/")
            formatted = {"lat": coordinates[0], "lng": coordinates[1]}
            payload = json.dumps(formatted)  
            
            
            client.publish(MQTT_TOPIC, payload)
            print(f"Sent: {payload}")


except KeyboardInterrupt:
    print("\nStopping MQTT publisher...")
    client.disconnect()
