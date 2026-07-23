# INSTALL azure-eventhub before running!
# pip command:
# pip install azure-eventhub

from azure.eventhub import EventHubProducerClient, EventData
from datetime import datetime, timezone
import hashlib
import random
import time
import json
