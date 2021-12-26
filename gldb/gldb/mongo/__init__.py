import os
import pymongo
from dotenv import load_dotenv

load_dotenv('../.env')

class MongoClient(object):
    """Connect to MongoDB"""

    def __init__(self):
        self.client = None
    
    def __enter__(self):
        self.client = pymongo.MongoClient(
            username=os.environ['MONGO_USERNAME'],
            password=os.environ['MONGO_PASSWORD'],
            host=os.environ['MONGO_HOSTNAME'],
            port=int(os.environ['MONGO_PORT']),
        )
        return self.client
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
