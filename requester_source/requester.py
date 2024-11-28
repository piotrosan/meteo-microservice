import requests
from resources import EdwinRequestResource
from requests import Request, Session


class Requester:
    resources = EdwinRequestResource()
    session = Session()

    def header(self):
        pass

    def get_stations(self) -> requests.Response:
        url, method = self.resources.list_stations_url()
        r = Request(method, url=url)
        return self.session.send(self.session.prepare_request(r))

    def get_station(
            self,
            path_params: str
    ) -> requests.Response:
        url, method = self.resources.get_station_url(path_params)
        r = Request(method, url=url)
        return self.session.send(self.session.prepare_request(r))

    def get_meteorological_data(
            self,
            path_params: str,
            params: dict = None
    ) -> requests.Response:
        url, method = self.resources.get_meteo_data_from_station(path_params)
        r = Request(method, url=url)
        if not params:
            r.params(params)
        return self.session.send(self.session.prepare_request(r))
