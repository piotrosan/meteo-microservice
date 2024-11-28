from dataclasses import dataclass


@dataclass
class EdwinRequestResource:
    base: str = 'https://edwin-meteo.apps.paas.psnc.pl'
    station: str = '/observationStation'
    meteo_data: str = '/meteo/station'

    def list_stations_url(self) -> (str, str):
        return f'{self.base}{self.station}', 'GET'

    def get_station_url(self, station_id: str) -> (str, str):
        return f'{self.base}{self.station}/{station_id}', 'GET'

    def get_meteo_data_from_station(self, station_id: str) -> (str, str):
        return f'{self.base}{self.meteo_data}/{station_id}', 'GET'

