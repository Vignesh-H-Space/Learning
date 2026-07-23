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
EVENTHUB_NAME = 'esehpnhxzayrvu14rciul9_eh'
CONNECTION_STR = 'Endpoint=sb://esehpnhxzayrvu14rciul9.servicebus.windows.net/;SharedAccessKeyName=key_32b6eb82-9b23-444b-aaad-7237aedcf71f;SharedAccessKey=KkpUeaWS4FphQyP/REmzoDpZ2XYsOIab3+AEhMsqG00=;EntityPath=esehpnhxzayrvu14rciul9_eh'


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
