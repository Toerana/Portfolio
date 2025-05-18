#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFiManager.h>

bool flag; // flag de reconexion du wifi

const int boutonPin = 2;   // Broche où le bouton est connecté
const int ledPin = 14;     // Broche où la LED est connectée

int etatBouton = 0;        // Variable pour stocker l'état du bouton
int etatPrecedent = 0;     // Variable pour stocker l'état précédent du bouton
int etatLED = LOW;         // État initial de la LED (éteinte)
int etatLEDPrecedent = LOW; 

const char* mqtt_client_name= "Prise2"; // Nom du client pour le Brocker
const char* mqtt_server ="broker.hivemq.com"; // adresse du Broker
const int mqtt_port =1883 ; // Port de communication 
const char* mqtt_topic ="SAE31/Home"; //Topic de send et receve

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(boutonPin, INPUT);
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
  
  // Crée un objet WiFiManager
  WiFiManager wifiManager;

  // Initialise WiFiManager et connecte ou configure le Wi-Fi si nécessaire
  if (!wifiManager.autoConnect("Prise2")) {
    Serial.println("Échec de la connexion et mise en place du portail de configuration");
    delay(3000);
    // Réinitialise et réessaie
    ESP.reset();
    delay(5000);
  }

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(Message_Recu);
  reconnect();
}

void loop() {
  //verifie la connexion au MQTT
  if (!client.connected()) {
    reconnect();
  }
  // Vérifie si des messages ont été reçus du serveur
  client.loop();
  
  etatBouton = digitalRead(boutonPin);

  // Vérifie si le bouton a été enfoncé
  if (etatBouton == HIGH && etatPrecedent == LOW) {
    // Inverse l'état de la LED
    etatLED = !etatLED;
    digitalWrite(ledPin, etatLED);
  }
  etatPrecedent = etatBouton;
  
  // verifie si un meesage a été envoyer il y a moins d'une seconde sans bloquer le programe
  static unsigned long lastMsg = 0;
  if (millis() - lastMsg > 1000) {
    lastMsg = millis();
    // Envoi du message MQTT
    if (client.connected()) {
      client.publish(mqtt_topic, ("prise:prise2/state:" + String(etatLED)).c_str());
    }
  }
}

void Message_Recu(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message reçu [");
  Serial.print(topic);
  Serial.print("] ");

  // Construit la chaîne de caractères à partir du payload
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.println(message);

  // Vérifie si le message concerne la prise 1
  if (strstr(message.c_str(), "prise:prise2/") != NULL) {
    // Extrait l'état du message
    String stateString = message.substring(message.indexOf("state:") + 6);
    int state = stateString.toInt();

    // Vérifie si l'état a vraiment changé
    if (state != etatLEDPrecedent) {
      // Met à jour l'état de la LED
      etatLEDPrecedent = state;

      if (state == 1) {
        etatLED = HIGH;
        digitalWrite(ledPin, etatLED);
        Serial.println("LED allumée");
      } else {
        etatLED = LOW;
        digitalWrite(ledPin, etatLED);
        Serial.println("LED éteinte");
      }
    }
  }
}

void reconnect() {
  // Boucle jusqu'à ce que nous soyons reconnectés
  while (!client.connected()) {
    Serial.print("Tentative de connexion MQTT...");
    if (client.connect(mqtt_client_name)) {
      Serial.println("Connecté");
      // Abonnement au topic
      client.subscribe(mqtt_topic);
    }
  }
}
