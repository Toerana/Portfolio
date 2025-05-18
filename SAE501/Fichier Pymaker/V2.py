from network import LoRa
import socket
import time
import ubinascii
import struct
import pycom
import binascii
from LIS2HH12 import LIS2HH12
from L76GNSS import L76GNSS
from pycoproc_1 import Pycoproc

pytrack = Pycoproc(Pycoproc.PYTRACK)
acc = LIS2HH12()
acc.enable_activity_interrupt(2000, 200)
gps = L76GNSS(pytrack, timeout=42, buffer=411)

# Definition du LoRan pour les fréquences EU
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Identifiant de connexion LoRa
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('0C96E3D1199620730AFC1FFA3203DC8D')
dev_eui = ubinascii.unhexlify('70B3D5499BD6A27C')

# Connection au LoRa en utilisant les identifiant précédent
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# attente pendant les essaies de connexions
while not lora.has_joined():
    pycom.rgbled(0xFF0000)
    time.sleep(2.5)
    print('Not yet joined...')

# LoRan Connecter
print('Joined')
pycom.rgbled(0x00FF00)

# Creation du socket LoRa
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Definition du Data Rate 5 = SF7 125kHz
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# Definition du Socket en non bloquer pour ne pas attendre dans un état de récéption
s.setblocking(False)

#Liste des coordonées qui seront envoyer
coordinate = [[49.0581,4.3623],[47.0023,9.3527],[38.0853,1.3274],[21.0255,2.3562]]
point_gps = 0

def encode_gps(lat, lon):
    lat_encoded = int(((lat + 90) / 180) * (2**24 - 1))
    lon_encoded = int(((lon + 180) / 360) * (2**24 - 1))
    return bytes([
        (lat_encoded >> 16) & 0xFF, # Octet de poids fort de la latitude
        (lat_encoded >> 8) & 0xFF, # Octet du milieu
        lat_encoded & 0xFF, # Octet de poids faible
        (lon_encoded >> 16) & 0xFF, # Octet de poids fort de la longitude
        (lon_encoded >> 8) & 0xFF, # Octet du milieu
        lon_encoded & 0xFF # Octet de poids faible
    ])

time.sleep(1)
while not acc.activity():
    pycom.rgbled(0x000000)
    time.sleep(0.1)

# check if we were awaken due to activity
if acc.activity():
    pycom.rgbled(0xFF0000)
    time.sleep(0.5)
    pycom.rgbled(0x00FF00)
    time.sleep(0.5)
    pycom.rgbled(0x0000FF)
    time.sleep(0.5)
    # Send GPS Data
    while True:
        pycom.rgbled(0x00FF00)
        lat, lon = gps.coordinates(debug=True)
        if lat is None or lon is None:
            print ('Aucune coordonée gps cordonées aléatoires')
            if point_gps == 3:
                point_gps == 0
            #Récupération des coordonée et formatage en entier
            coord = coordinate[point_gps]
            lat = coord[0]
            lon = coord[1]
        print (lat)
        print (lon)
        coord_byte = encode_gps(lat,lon)
        print ("Envoie des cordonées suivantes : ",coord)
        print (coord_byte)

        time.sleep(1)
        pycom.rgbled(0x0000FF) #Led en bleu indique l'envoie
        s.send(coord_byte) #Envoie

        point_gps += 1
        time.sleep(1)
        pycom.rgbled(0xFC8C03)# led orange
        time.sleep(150) #attente de 150 seconde pour respecter 99IT
