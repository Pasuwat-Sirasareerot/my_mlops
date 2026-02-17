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
        except Exception as e:
            raise ProjectException(e, sys)