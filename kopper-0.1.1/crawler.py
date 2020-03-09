from datetime import datetime

import requests
from requests import Session

from helper import get_name_from_code

from constants.parameters import PARAMETERS
from constants.days import DAYS
from constants.stations import STATIONS
from constants.train_type import TRAIN_TYPE
from constants.links import LINKS

class Crawler(object):

    def __init__(self):
        self._session = Session()

    def trains_info(self, depart_date, depart_time, departure, arrival, train_type):
        _params = PARAMETERS.train_info.value
        
        _date = datetime.strptime(depart_date, "%Y%m%d")
        _time = datetime.strptime(depart_time, "%H%M%S")
        
        _params.update({
            "selGoDay"      : '{:02d}'.format(_date.day),       # selected depart day
            "selGoHour"     : '{:02d}'.format(_time.hour),      # selected depart hour (HH)
            "selGoMonth"    : '{:02d}'.format(_date.month),     # selected depart month
            "selGoTrain"    : train_type.value,     # train type code
            "selGoYear"     : '{:d}'.format(_date.year),        # selected depart year
            "start"         : datetime.strftime(_date, "%Y.%m.%d").replace(".0", "."), # selected depart date (yyyy.M.d)
            "txtGoAbrdDt"   : datetime.strftime(_date, "%Y%m%d"), # selected depart date (yyyyMMdd)
            "txtGoEnd"      : get_name_from_code(STATIONS, arrival.value),        # arrival station name
            "txtGoHour"     : depart_time,                      # selected depart time (HHmmss)
            "txtGoStart"    : get_name_from_code(STATIONS, departure.value),      # department station name
            "txtGoYoil"     : get_name_from_code(DAYS, _date.weekday()),    # selected a day code of the week.
        })

        response = self._session.post(LINKS.train_info.value, data=_params)
        html = response.text

        return response.status_code, html

    def train_routes(self, train):
        return self._train_route(train.run_date, train.depart_date, train.train_no, train.train_group_code)

    def _train_route(self, run_date, depart_date, train_no, train_group_code):
        _params = PARAMETERS.route_info.value

        _params.update({
            'txtRunDt': run_date,       # YYYYmmdd
            'txtDptDt': depart_date,    # YYYYmmdd
            'txtTrnNo': train_no,
            'txtTrnGpCd': train_group_code,
        })

        response = requests.get(LINKS.route_info.value, params=_params)
        html = response.text

        return response.status_code, html
