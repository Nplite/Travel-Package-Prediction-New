import pymongo
import pandas as pd
import os,sys
import json
from dataclasses import dataclass



@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "MonthlyIncome"
print(env_var.mongo_db_url)