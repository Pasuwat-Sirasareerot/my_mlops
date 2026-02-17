import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import ProjectException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL_KEY")

print(MONGODB_URL)

import certifi
ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise ProjectException(e, sys)
        
    def csv_to_json(self, file_path):
        try:
            ds = pd.read_csv(file_path)
            ds.reset_index(inplace=True, drop=True)
            records = list(json.loads(ds.T.to_json()).values())
            return records
        except Exception as e:
            raise ProjectException(e, sys)
        
    def insert_data_to_database(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            self.database =self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return (len(self.records))
        except Exception as e:
            raise ProjectException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "/Users/yarida/Desktop/mlops_learning/network_data/phisingData.csv"
    DATABASE = "pasuwat_db"
    COLLECTION = "phishing_data"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(file_path=FILE_PATH)
    print(f"{len(records)} records found in csv file")
    no_record = networkobj.insert_data_to_database(records, DATABASE, COLLECTION)
    print(f"{no_record} records inserted to database {DATABASE} and collection {COLLECTION}")