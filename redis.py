import redis
import json

# Connect to the Redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Simulate sensor readings
sensor_readings = [
    {
        "sensor_id": "sensor1",
        "value": 25.5,
        "timestamp": "2023-09-18T12:00:00Z"
    },
    {
        "sensor_id": "sensor2",
        "value": 30.1,
        "timestamp": "2023-09-18T12:05:00Z"
    },
    # Add more readings here
]

# Store the latest ten readings in Redis
for reading in sensor_readings[-10:]:
    r.lpush("sensor_readings", json.dumps(reading))

