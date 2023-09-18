
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

app = FastAPI()

# Sample data (replace with your actual sensor data)
sensor_data = [
    {"sensor_id": "sensor1", "value": 25.5, "timestamp": "2023-09-18T10:00:00"},
    {"sensor_id": "sensor2", "value": 30.1, "timestamp": "2023-09-18T10:10:00"},
    # Add more sensor readings here
]

@app.get("/sensor-readings/")
async def get_sensor_readings(start: str, end: str) -> List[dict]:
    """
    Get sensor readings within a specified time range.
    Example usage: /sensor-readings/?start=2023-09-18T10:00:00&end=2023-09-18T10:30:00
    """
    readings_within_range = [
        reading for reading in sensor_data if start <= reading["timestamp"] <= end
    ]
    if not readings_within_range:
        raise HTTPException(status_code=404, detail="No readings found within the specified range.")
    return readings_within_range

@app.get("/sensor-last-ten-readings/")
async def get_last_ten_sensor_readings(sensor_id: str) -> List[dict]:
    """
    Get the last ten sensor readings for a specific sensor.
    Example usage: /sensor-last-ten-readings/?sensor_id=sensor1
    """
    last_ten_readings = [
        reading for reading in sensor_data if reading["sensor_id"] == sensor_id
    ][:10]
    if not last_ten_readings:
        raise HTTPException(status_code=404, detail=f"No readings found for sensor {sensor_id}.")
    return last_ten_readings

