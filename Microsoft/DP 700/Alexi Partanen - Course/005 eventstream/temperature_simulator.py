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
