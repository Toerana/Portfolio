const int boutonPin = 2;   // Broche où le bouton est connecté
const int ledPin = 14;     // Broche où la LED est connectée

int etatBouton = 0;        // Variable pour stocker l'état du bouton
int etatPrecedent = 0;     // Variable pour stocker l'état précédent du bouton
int etatLED = LOW;         // État initial de la LED (éteinte)

void setup() {
  pinMode(boutonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  etatBouton = digitalRead(boutonPin);

  // Vérifie si le bouton a été enfoncé
  if (etatBouton == HIGH && etatPrecedent == LOW) {
    // Inverse l'état de la LED
    etatLED = !etatLED;
    digitalWrite(ledPin, etatLED);
  }

  etatPrecedent = etatBouton;
}
