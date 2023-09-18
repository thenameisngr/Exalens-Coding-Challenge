
import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

# MQTT Broker Settings
broker_address = "mqtt_broker"
port = 1883
topic_temperature = "sensors/temperature"
topic_humidity = "sensors/humidity"

# Function to generate random sensor data
def generate_sensor_data(sensor_id):
    value = round(random.uniform(0, 100), 2)
    timestamp = datetime.now().isoformat()
    payload = {
        "sensor_id": sensor_id,
        "value": value,
        "timestamp": timestamp
    }
    return json.dumps(payload)

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create MQTT client
client = mqtt.Client()

# Set on_connect callback
client.on_connect = on_connect

# Connect to MQTT broker
client.connect(broker_address, port, 60)

try:
    while True:
        # Generate random sensor data for temperature and humidity
        temperature_data = generate_sensor_data("temperature_sensor_1")
        humidity_data = generate_sensor_data("humidity_sensor_1")

        # Publish data to MQTT topics
        client.publish(topic_temperature, temperature_data)
        client.publish(topic_humidity, humidity_data)

        print(f"Published data: {temperature_data}")
        print(f"Published data: {humidity_data}")

        # Wait for some time before publishing again (e.g., every 5 seconds)
        time.sleep(5)

except KeyboardInterrupt:
    client.disconnect()


