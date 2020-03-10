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
            "selGoTrain"    : train_type.value[0] if type(train_type.value) is tuple else train_type.value,     # train type code
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

    def train_srcar_length(self, train):
        _params = PARAMETERS.srcar_length_info.value

        _params.update({
            'txtArvRsStnCd': '{:04d}'.format(int(train.arrival_station_code)),      # arrival station code (NNNN: zero filed)
            'txtArvStnRunOrdr': train.raw_train_info['h_arv_stn_run_ordr'],         # used by train instance (NNNNNN:zero filed)
            'txtArvTm': train.arrival_time,                                         # arrival time (HHMMSS)
            'txtDptDt': train.depart_date,                                          # depart date (YYYYmmdd)
            'txtDptRsStnCd': '{:04d}'.format(int(train.depart_station_code)),       # depart station code (NNNN: zero filed)
            'txtDptStnRunOrdr': train.raw_train_info['h_dpt_stn_run_ordr'],         # used by train instance (NNNNNN:zero filed)
            'txtDptTm': train.depart_time,                                          # depart time (HHMMSS)
            'txtPsrmClCd': '1',
            'txtRunDt': train.depart_date,                                          # depart date (YYYYmmdd)
            'txtSeatAttCd': '015',
            'txtSrcarNo': '1',
            'txtTotPsgCnt': '1',
            'txtTrnClsfCd': train.train_classification_code,                        # train's classification code
            'txtTrnGpCd': train.train_group_code,                                   # train's group code
            'txtTrnNo': train.train_no,                                             # train's no
        })

        response = requests.get(LINKS.srcar_length_info.value, params=_params)
        html = response.text

        return response.status_code, html


    def train_seats_by_schedule(self, train, schedule, srcar_length):
        seats_info = {}
        
        for route in schedule.sorted_routes:
            seats_info[route] = {}
            
            for srcar_no in srcar_length:
                _, html = self.train_seat_by_route(train, route, srcar_no)
                seats_info[route][srcar_no] = html

        return seats_info


    def train_seat_by_route(self, train, route, srcar_no):
        _params = PARAMETERS.seat_info.value

        _params.update({
            'txtArvRsStnCd': '{:04d}'.format(int(route.next_station_code)),     # arrival station code (NNNN: zero filed)
            'txtArvStnRunOrdr': '{:06d}'.format(route.arrival_order),           # used by train instance (NNNNNN:zero filed)
            'txtDptRsStnCd': '{:04d}'.format(int(route.station_code)),          # depart station code (NNNN: zero filed)
            'txtDptStnRunOrdr': '{:06d}'.format(route.depart_order),            # used by train instance (NNNNNN:zero filed)
            'txtRunDt': train.depart_date,                                      # depart date (YYYYmmdd)
            'txtSrcarNo': srcar_no,                                             # selected #. of 'arrSrcarNo'
            'txtTrnClsfCd': train.train_classification_code,                    # train's classification code
            'txtTrnGpCd': train.train_group_code,                               # train's group code
            'txtTrnNo': train.train_no,                                         # train's no
        })

        response = self._session.post(LINKS.seat_info.value, data=_params)
        html = response.text

        return response.status_code, html
          