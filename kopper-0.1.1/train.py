from datetime import datetime

from helper import get_name_from_code
from constants.train_type import TRAIN_TYPE

class Train(object):

    def __init__(self, raw_train_info):
        self.raw_train_info = raw_train_info
        self._initialize()
    
    def _initialize(self):
        raw_info = self.raw_train_info

        self._arrival_date = datetime.strptime(raw_info['h_arv_dt'], '%Y%m%d')
        self._arrival_station_code = '{:02d}'.format(int(raw_info['h_arv_rs_stn_cd']))
        self._arrival_station_name = raw_info['h_arv_rs_stn_cd_nm']
        self._arrival_time = datetime.strptime(raw_info['h_arv_tm'], '%H%M%S')
        
        self._depart_date = datetime.strptime(raw_info['h_dpt_dt'], '%Y%m%d')
        self._depart_station_code = '{:02d}'.format(int(raw_info['h_dpt_rs_stn_cd']))
        self._depart_station_name = raw_info['h_dpt_rs_stn_cd_nm']
        self._depart_time = datetime.strptime(raw_info['h_dpt_tm'], '%H%M%S')

        self._train_no = raw_info['h_trn_no']
        self._train_type_code = raw_info['h_trn_clsf_cd']
        self._train_type_name = get_name_from_code(TRAIN_TYPE, self._train_type_code)
        self._train_group_code = raw_info['h_trn_gp_cd']

        self._run_date = datetime.strptime(raw_info['h_run_dt'], '%Y%m%d')
        self._delay_hour = datetime.strptime(raw_info['h_dlay_hr'], '%H%M%S')

    @property
    def arrival_date(self):
        return datetime.strftime(self._arrival_date, '%Y%m%d')

    @property
    def arrival_station_code(self):
        return self._arrival_station_code

    @property
    def arrival_station_name(self):
        return self._arrival_station_name

    @property
    def arrival_time(self):
        return datetime.strftime(self._arrival_time, '%H%M%S')

    @property
    def depart_date(self):
        return datetime.strftime(self._depart_date, '%Y%m%d')

    @property
    def depart_station_code(self):
        return self._depart_station_code

    @property
    def depart_station_name(self):
        return self._depart_station_name

    @property
    def depart_time(self):
        return datetime.strftime(self._depart_time, '%H%M%S')
      
    @property
    def train_no(self):
        return self._train_no
      
    @property
    def train_type_code(self):
        return self._train_type_code

    @property
    def train_type_name(self):
        return self._train_type_name

    @property
    def train_group_code(self):
        return self._train_group_code

    @property
    def run_date(self):
        return datetime.strftime(self._run_date, '%Y%m%d')

    @property
    def delay_hour(self):
        return datetime.strftime(self._delay_hour, '%H%M%S')


    def __str__(self):
        # No.00101 \t KTX \t 서울(05:15) ------ 부산(07:51)
        return 'No.{} \t {} \t {}({}) ------ {}({})'.format(
            self.train_no, self.train_type_name,
            self.depart_station_name, self.depart_time,
            self.arrival_station_name, self.arrival_time
            )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
