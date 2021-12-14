# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

import pymongo
from . import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_collection = database['users']

async def present_in_userbase(user_id : int):
    found = user_collection.find_one({'_id': user_id})
    return bool(found)

async def add_to_userbase(user_id: int):
    user_collection.insert_one({'_id': user_id})
    return

async def get_users():
    user_docs = user_collection.find()
    return [doc['_id'] for doc in user_docs]
    
async def del_from_userbase(user_id: int):
    user_collection.delete_one({'_id': user_id})
    return