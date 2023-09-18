
import paho.mqtt.client as mqtt
import pymongo
import json

# MQTT broker configuration
mqtt_broker_host = "mqtt_broker"  # Replace with your MQTT broker hostname
mqtt_topic = "sensors/temperature"  # MQTT topic to subscribe to

# MongoDB configuration
mongo_client = pymongo.MongoClient("mongodb://mongodb_host:27017/")  # Replace with your MongoDB host
mongo_db = mongo_client["mydb"]  # Replace with your database name
mongo_collection = mongo_db["sensor_data"]  # Replace with your collection name

# MQTT message callback
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    mongo_collection.insert_one(payload)
    print(f"Received and stored message: {payload}")

# Create an MQTT client
mqtt_client = mqtt.Client()

# Set up the message callback
mqtt_client.on_message = on_message

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker_host, 1883)  # Use the correct MQTT port

# Subscribe to the MQTT topic
mqtt_client.subscribe(mqtt_topic)

# Start the MQTT loop to listen for messages
mqtt_client.loop_forever()

