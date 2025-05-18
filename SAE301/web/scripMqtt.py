import paho.mqtt.client as mqtt
import pymysql.cursors
from datetime import datetime
# Connexion à la base de données MySQL

brocker_address = '192.168.228.192'
topic = 'SAE31/Home'
#TODO Check le nom du brocker et le topic
def create_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='toto',
            db='django_mura',
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f'Successful connection with MySQL version {pymysql.__version__}')
    except pymysql.Error as e:
        print(f'An error {e.args[0]} occurred')
    return conn



def insert_data(conn, prise, etat):
    with conn.cursor() as cursor:
        sql = """
        UPDATE sae_app_values SET etat = %s WHERE prise = %s; 	
        """
        cursor.execute(sql, (etat, prise))
        conn.commit()
        print('Sensor history data inserted into \'data\' successfully')
    
def on_message(client, userdata, msg):
    print(f'Received message: {msg.topic} {msg.payload.decode()}')

    # Analyse du message MQTT pour extraire les données
    data = msg.payload.decode().split('/')
    data_dict = {item.split(':')[0]: item.split(':')[1] for item in data}
   
    prise = data_dict.get('prise')
    etat = data_dict.get('state')
   
    insert_data(userdata,prise= prise,etat=etat)



client = mqtt.Client()
client.user_data_set(create_connection())
client.on_message = on_message
client.connect(brocker_address)
client.subscribe(topic)
client.loop_forever()

