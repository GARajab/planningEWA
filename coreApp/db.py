# db.py
from pymongo import MongoClient
from django.conf import settings

# MongoDB connection URI
uri = "mongodb+srv://garajab24:Rajab102030@webbasedapps.crz8f.mongodb.net/planning?retryWrites=true&w=majority"

# Initialize MongoDB client
client = MongoClient(uri)

# Access the database
db = client.planning

# Define collections
COLLECTION_DEPOT2024 = db.Depot2024
COLLECTION_DEPOT2025 = db.Depot2025
COLLECTION_LR2024 = db.lr24
COLLECTION_LR2025 = db.lr2025
COLLECTION_NC2024 = db.nc2024
