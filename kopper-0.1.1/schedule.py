class Schedule(object):

    def __init__(self, routes):
        self.routes = []

        if routes:
            self.routes = routes

        self.sorted_routes = sorted(self.routes)

    def add_route(self, route):
        if route not in self.routes:
            self.routes.append(route)
        
        self.sorted_routes = sorted(self.routes)

    def __str__(self):
        # 서울 (14:00) - 광명 (14:14)
        # 광명 (14:16) - 오송 (14:43)
        # 오송 (14:45) - 대전 (15:00)
        # 대전 (15:02) - 동대구 (15:45)
        # 동대구 (15:47) - 부산 (16:27)
        msg = ''
        for route_depart, route_arrival in zip(self.sorted_routes[:-1], self.sorted_routes[1:]):
            msg += '{} ({}) - {} ({}) \n'.format(
                route_depart.station_name, route_depart.depart_time,
                route_arrival.station_name, route_arrival.arrival_time,
            )

        return msg.strip()
