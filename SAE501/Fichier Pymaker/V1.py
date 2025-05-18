from network import LoRa
import socket
import time
import ubinascii
import struct
import pycom
from machine import UART

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

# Send GPS Data
while True:
    pycom.rgbled(0x00FF00)
    if point_gps == 3:
        point_gps == 0
    #Récupération des coordonée et formatage en entier
    coord = coordinate[point_gps]
    lat = str(int(coord[0] * 10**4))
    lon = str(int(coord[1] * 10**4))
    #print ("Envoie des cordonées suivantes : "+coord)

    """
        Decoupe les coordonées en 4 2 latitude et 2 longitude
        Afin de préparer l'envoie on la partie une est comprise entre -18099 et 18099
        la deuxsième partie est comprise entre 0 et 99 le découpage est différent selon le signe et la longeur du nombre
    """
    if len(lat) >= 7:
        div = 5
    else:
        div = 4
    if lat [0] == '-':
        div = div+1
        lat1 = int(lat[:div])
        lat2 = int(lat[div:])
    else:
        lat1 = int(lat[:div])
        lat2 = int(lat[div:])
    if len(lon) >= 7:
        div = 5
    else:
        div = 4
    if lon [0] == '-':
        div = div+1
        lon1 = int(lon[:div])
        lon2 = int(lon[div:])
    else:
        lon1 = int(lon[:div])
        lon2 = int(lon[div:])

    #Création du payload en byte selon le format (2 Octets signé 1 Octet non signé * 2)
    payload = struct.pack(">hBhB", lat1,lat2,lon1,lon2)
    time.sleep(1)
    pycom.rgbled(0x0000FF) #Led en bleu indique l'envoie
    s.send(payload) #Envoie

    point_gps += 1
    time.sleep(1)
    pycom.rgbled(0xFC8C03)#led orange indique
    time.sleep(150) #attente de 150 seconde pour respecter 99IT