from datetime import datetime, timedelta

from constants.stations import STATIONS

class Route(object):

    def __init__(self, raw_route_info):
        self._raw_route_info = raw_route_info
        self._seats_info = {}

        self._depart_order = self._arrival_order = 0
        self._next_station_code = 0
        self._next_station_name = ''

        self._initalize()

    def _initalize(self):
        raw_info = self._raw_route_info

        self._station_name = raw_info['station_name']
        
        # 울산(통도사) -> 울산_통도사
        self._station_name = '울산_통도사' if self._station_name == '울산(통도사)' else self._station_name
            
        # TODO Exception if self._station_name is not a key of STATIONS.
        self._station_code = STATIONS[self._station_name].value

        self._arrival_time = datetime.strptime(raw_info['arrival_time'], '%H:%M')
        self._depart_time = datetime.strptime(raw_info['depart_time'], '%H:%M')
        
        self._delta_delay_minutes = timedelta(int(raw_info['delay_minutes']))
        self._delayed_arrival_time = self._arrival_time + self._delta_delay_minutes

    @property
    def station_name(self):
        return self._station_name
        
    @property
    def station_code(self):
        return self._station_code

    @property
    def arrival_time(self):
        return datetime.strftime(self._arrival_time, '%H:%M')
        
    @property
    def depart_time(self):
        return datetime.strftime(self._depart_time, '%H:%M')

    @property
    def delayed_arrival_time(self):
        return datetime.strftime(self._delayed_arrival_time, '%H:%M')
    
    @property
    def delay_minutes(self):
        return self._delta_delay_minutes.seconds // 60

    
    @property
    def depart_order(self):
        return self._depart_order
    
    @property
    def arrival_order(self):
        return self._arrival_order

    @property
    def next_station_code(self):
        return self._next_station_code

    @property
    def next_station_name(self):
        return self._next_station_name

    @property
    def seats_info(self):
        return self._seats_info
        
    @depart_order.setter
    def depart_order(self, order):
        self._depart_order = order
    
    @arrival_order.setter
    def arrival_order(self, order):
        self._arrival_order = order

    @next_station_code.setter
    def next_station_code(self, code):
        self._next_station_code = code

    @next_station_name.setter
    def next_station_name(self, name):
        self._next_station_name = name

    @seats_info.setter
    def seats_info(self, info):
        self._seats_info = info


    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self.__dict__ == other.__dict__
        return False

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time

    def __hash__(self):
        return hash((
            self.station_name, 
            self.station_code, 
            self.depart_time, 
            self.arrival_time
        ))