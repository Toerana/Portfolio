import threading
import paho.mqtt.client as mqtt
import time
# Configuration
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "gps/coordinates/rom"

# Create and configure MQTT client
client = mqtt.Client()

# Callback for when a message is received
def on_message(client, userdata, msg):

    print(f"\n\nReceived message at {time.strftime('%H:%M')}: '{msg.payload.decode()}' on topic '{msg.topic}'\n\n")

client.on_message = on_message  # Attach the callback

try:
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

# Start the MQTT loop in a separate thread
def mqtt_loop():
    client.subscribe(MQTT_TOPIC)  # Subscribe to the topic
    client.loop_forever()  # Start processing messages

# Start the reception thread
receiver_thread = threading.Thread(target=mqtt_loop, daemon=True)
receiver_thread.start()

try:
    while True:
        msg = input("")
        if msg.strip():
            result = client.publish(MQTT_TOPIC, msg)

            status = result[0]
            if status == 0:
                print(f"Sent: {msg}")
            else:
                print(f"Failed to send message to topic {MQTT_TOPIC}")
except KeyboardInterrupt:
    print("\nStopping MQTT sender...")
finally:
    client.disconnect()
