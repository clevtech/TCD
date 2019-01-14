import pymongo
from pymongo import MongoClient
from tqdm import tqdm

client = MongoClient('localhost', 27017)
db = client.NOtest
collection = db.old

def insert(post):
    return collection.insert_one(post).inserted_id

import json

with open('database.json', 'r') as f:
    array = json.load(f)


for el in tqdm(array):
    insert(el)
