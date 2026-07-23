# INSTALL azure-eventhub before running!
# pip command:
# pip install azure-eventhub

from azure.eventhub import EventHubProducerClient, EventData
from datetime import datetime, timezone
import hashlib
import random
import time
import json

# Replace the placeholders with your Event Hubs connection string and event hub name
EVENTHUB_NAME = 'Redacted'
CONNECTION_STR = 'Redacted'

# Configuration variables
MIN_TEMPERATURE = 19.0          # Minimum temperature value
MAX_TEMPERATURE = 20.0          # Maximum temperature value
COUNTRY = "USA"                 # Country
CITY = "new york"               # City
SLEEP_TIME = 3                  # Sleep time before sending next event

# Create a producer client to send messages to the event hub
producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)

def generate_fake_temperature(min_temp, max_temp):
    """Simulate a fake temperature reading within the specified range or generate null."""
    return str(round(random.uniform(min_temp, max_temp), 2))

def get_random_sensor_readings(min_temp, max_temp):
    """Generate a list of temperature readings for random sensors."""
    sensors = ["sensor_1", "sensor_2", "sensor_3"]
    selected_sensors = random.sample(sensors, random.randint(1, len(sensors)))
    return [{"sensor": sensor, "temperature": generate_fake_temperature(min_temp, max_temp)}
            for sensor in selected_sensors]
    
def generate_event_id(payload):
    """Generate a SHA256 hash as a unique event ID."""
    hash_object = hashlib.sha256(json.dumps(payload, sort_keys=True).encode('utf-8'))
    return hash_object.hexdigest()

def get_current_timestamp():
    """Return the current timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


try:
    # Continuously generate and send fake temperature readings
    while True:
        # Create a batch.
        event_data_batch = producer.create_batch()
        
        # Generate random sensor readings
        temperature_readings = get_random_sensor_readings(MIN_TEMPERATURE, MAX_TEMPERATURE)
        
        # Create the payload
        payload = {
            "country": COUNTRY,
            "city": CITY,
            "timestamp": get_current_timestamp(),
            "temperature_readings": temperature_readings
        }
        
        # Generate an event_id
        payload["event_id"] = generate_event_id(payload)
        
        # Format the message as JSON
        message = json.dumps(payload)

        # Add the JSON-formatted message to the batch
        event_data_batch.add(EventData(message))
        
        # Send the batch of events to the event hub
        producer.send_batch(event_data_batch)
        
        print(json.dumps(json.loads(message), indent=4))
        print(event_data_batch)
        
        # Wait for a bit before sending the next reading
        time.sleep(SLEEP_TIME)
