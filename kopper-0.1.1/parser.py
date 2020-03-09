import re

from bs4 import BeautifulSoup

from constants.parsing_map import PARSING_MAP

def parsing_raw_trains_info(html):
    rgx_pattern = r'train_info\((.*)\)'

    soup = BeautifulSoup(html, "html.parser")

    js_soup_tags = soup.find_all("script", {"type": "text/javascript", "language": "javascripts"})

    trains = []

    for js_soup in js_soup_tags:
        js_text = ''.join(js_soup.text.split())
        raw_train_info = re.search(rgx_pattern, js_text).group(1).replace('"', "").split(",")

        assert(len(PARSING_MAP.train_info.value) == len(raw_train_info))

        train_info = dict(zip(PARSING_MAP.train_info.value, raw_train_info))
        trains.append(train_info)

    if not trains:
        raise ValueError("""Trains information is not responsed.
            Probably the parmaters of Crawler.trains_info's passed are not valid.
            Please execute Crawler.trains_info function, again.
            """)

    return trains


def parsing_raw_train_routes(html):
    soup = BeautifulSoup(html, "html.parser")

    tbody_tag = soup.find("tbody")
    tr_tags = tbody_tag.find_all("tr")


    routes = []
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all("td")

        station_name = td_tags[0].text.strip()
        arrival_time = '00:00' if td_tags[1].text.strip() == '-' else td_tags[1].text.strip()
        depart_time = '00:00' if td_tags[2].text.strip() == '-' else td_tags[2].text.strip()
        delay_minutes = '0' if td_tags[3].text.strip() == '-' else td_tags[3].text.strip()

        raw_route_info = [
            station_name,
            arrival_time,
            depart_time,
            delay_minutes,
        ]

        route_info = dict(zip(PARSING_MAP.route_info.value, raw_route_info))
        routes.append(route_info)

    if not routes:
        raise ValueError("""Schedule information is not responsed.
            Probably the parmaters of Crawler.schedule's passed are not valid.
            Please execute Crawler.trains_info function and pass train_info instance to Crawler.schedule, again.
            """)

    return routes