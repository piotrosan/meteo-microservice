import requests
import json

from pymongo.cursor import Cursor

from db.mongo_operations import MongoOperations


def save_stations_to_mongo_db(result: requests.Response):
    mo = MongoOperations()
    mo.set_active_database('weather')
    mo.set_active_collection('stations')
    content_data = result.json().get('content')
    if content_data:
        for cd in content_data:
            mo.save(cd)


def save_weather_data_to_mongo_db(result: requests.Response):
    mo = MongoOperations()
    mo.set_active_database('weather')
    mo.set_active_collection('weather_data')
    content_data = result.json().get('content')
    mo.save(content_data)


def get_all_stations() -> Cursor:
    mo = MongoOperations()
    mo.set_active_database('weather')
    mo.set_active_collection('stations')
    return mo.get_all()


