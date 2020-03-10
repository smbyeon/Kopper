class Schedule(object):

    def __init__(self, routes):
        self._routes = []

        if routes:
            self._routes = routes
        
        self._initialize()

    def _initialize(self):
        sorted_routes = sorted(self._routes)
        ordered_routes = []

        for idx, (route, route_next) in enumerate(zip(sorted_routes[:-1], sorted_routes[1:])):
            route.depart_order = idx + 1
            route.arrival_order = idx + 2

            route.next_station_code = route_next.station_code
            route.next_station_name = route_next.station_name

            ordered_routes.append(route)

        self._sorted_routes = ordered_routes

    # TODO
    def update_seats_info(self, route, seats_info):
        for idx, old_route in enumerate(self._routes):
            if old_route == route:
                route.seats_info = seats_info
                self._routes[idx] = route
                print(old_route)
                break


    @property
    def sorted_routes(self):
        return self._sorted_routes

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
