import os
from pymongo import MongoClient

class Config():
    # FUSION_AUTH = os.environ.get('AUTH')
    FUSION_URL = os.environ.get('FUSION_API_URL')
    PXE_SERVER_URL = os.environ.get('PXE_SERVER', '127.0.0.1:8069')
    RABBIT_MQ_SERVER = os.environ.get('RABBIT_MQ_SERVER', '10.0.0.2')
    MONGODB = os.environ.get('MONGODB_SERVER', '10.0.0.2')

class HostDB():
    client = MongoClient(Config.MONGODB)
    db = client.aperture
    INFO = db.nodes.find_one({}, { '_id': False })
