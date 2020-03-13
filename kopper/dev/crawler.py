import requests

from constants.links import LINKS
from constants.parameters import PARAMETERS

class Crawler(object):
    def stations_by_korean_idx(self, idx):
        # 가(0) - 하(13)
        _params = PARAMETERS.station_code_info.value
        _params.update({
            'hidKorInx': idx
        })

        response = requests.get(LINKS.station_code_info.value, params=_params)
        html = response.text

        return response.status_code, html