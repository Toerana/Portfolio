from network import WLAN
import machine
import time
import ubinascii
from mqtt import MQTTClient
from pycoproc_1 import Pycoproc  # Pytrack pour Pycom 2.0X
from L76GNSS import L76GNSS
import uos  # Pour générer des nombres aléatoires

WIFI_SSID = "S23+"
WIFI_PASS = "KikiLaMenace"

# Adresse brocker mqtt et publication
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "gps/coordinates/rom"
MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()

#connexion au wifi
wlan = WLAN(mode=WLAN.STA),
wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS))

print("Connexion au Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
print("Wi-Fi connecté! IP:", wlan.ifconfig()[0])

#connexion au brocker
def connect_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    client.connect()
    print("Connecté au broker MQTT")
    return client

client = connect_mqtt()

pytrack = Pycoproc(Pycoproc.PYTRACK)  # Initialize the PyTrack object
gps = L76GNSS(pytrack, timeout=42, buffer=411)

# coordonnées random autour et dans Colmar
def get_gps_coordinates():
    lat, lon = gps.coordinates(debug=True)
    if lat is None or lon is None:
        print("Aucune coordonnée GPS valide, génération de coordonnées aléatoires...")
        lat = round(48.0773 + (uos.urandom(1)[0] / 255 - 0.5) * 0.01, 6)
        lon = round(7.3709 + (uos.urandom(1)[0] / 255 - 0.5) * 0.01, 6)
    return lat, lon

# Envoie des données
try:
    while True:
        latitude, longitude = get_gps_coordinates()

        # Envoi MQTT
        mqtt_message = '{{"latitude": {}, "longitude": {}}}'.format(latitude, longitude)
        client.publish(topic=MQTT_TOPIC, msg=mqtt_message)
        print("MQTT envoyé :", mqtt_message)

        # Pause de 10 sec
        time.sleep(10)

except KeyboardInterrupt:
    print("Déconnexion...")
    client.disconnect()
