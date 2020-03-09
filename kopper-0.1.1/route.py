from datetime import datetime, timedelta

from constants.stations import STATIONS

class Route(object):

    def __init__(self, raw_route_info):
        self._raw_route_info = raw_route_info
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


    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self.__dict__ == other.__dict__
        return False

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time
