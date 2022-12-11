import pandas as pd
import numpy as np

from datetime import date, datetime
import time

import requests, urllib, json
from dotenv import dotenv_values
config = dotenv_values("./.env")

import pymongo

"""
Connect to MongoDB Atlas DataBase
"""
conn_str = (
   "mongodb+srv://"
   + urllib.parse.quote(config['MONGODB_USER']) 
   + ":"
   + urllib.parse.quote(config['MONGODB_PWD'])
   + "@hugoafsantos-datascienc.yvocwdh.mongodb.net/?retryWrites=true&w=majority"
)

client = pymongo.MongoClient(conn_str)
db = client['riotwatcher_api_fetch_data']

# print(db.command("collstats", "featured_match")["totalSize"]/1048576)
# print(db.command("dbstats")["storageSize"]/1048576)

"""
Retrieve all collections from 'riotwatcher_api_fetch_data' MongoDB instance 
"""
# print(db.list_collection_names())


"""
Use 'featured_match' collections and add/update/upsert/delete records 
"""
my_live_matches = db['my_live_matches']
# my_live_matches.drop()

# my_live_matches.delete_many({})

# from bson import ObjectId

# for record_id in my_live_matches.find():
#    print(ObjectId(record_id['_id']).generation_time)


""" 
Initialize Riot Game Client, League of Legends and Riot LiveClient
"""

url = "https://127.0.0.1:2999/liveclientdata/allgamedata"


""""
While 1 > 0: THEN ...
"""

while 1 > 0:
   time.sleep(5)
   
   response = requests.request("GET",url, verify=False) ### avoid CERTIFICATE_VERIFY_FAILED
   liveclientdata = response.json()

   my_live_matches.insert_one(liveclientdata)
   
    #  list_colls_featured_match[region_idx].update_one(
    #     {'gameId' : list_records_featured_match[record_idx]['gameId']},
    #     {'$set' : list_records_featured_match[record_idx]},
    #     upsert=True
    #  )

