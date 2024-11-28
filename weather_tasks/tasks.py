from main import app
from requester_source.requester import Requester
from business_logic.mongo_db_business_logic import (
    save_stations_to_mongo_db,
    save_weather_data_to_mongo_db,
    get_all_stations
)
from celery.schedules import crontab


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(minute='5'),
        update_stations_from_edwin,
        name='update edwin station'
    )

    sender.add_periodic_task(
        crontab(minute='6'),
        update_weather_data_from_edwin,
        name='update edwin weather data'
    )


@app.task
def update_stations_from_edwin():
    requester = Requester()
    result = requester.get_stations()
    save_stations_to_mongo_db(result)


@app.task
def update_weather_data_from_edwin():
    requester = Requester()
    stations = get_all_stations()
    for station in stations:
        result = requester.get_meteorological_data(
            station['id'], {'page': '0', 'size': '10'}
        )
        save_weather_data_to_mongo_db(result)

