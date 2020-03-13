import re

from bs4 import BeautifulSoup

def parsing_raw_stations_info(html):
    rgx_pattern = r'javascript:putStation\([\'\"]([\w\(\)]+)[\'\"], ?[\'\"](\w+)[\'\"]\)'
    
    soup = BeautifulSoup(html, "html.parser")

    div_tag = soup.find("div", {"class": "s_view"})
    tbody_tag = div_tag.find('tbody')
    a_tags = tbody_tag.find_all("a")

    stations = {}
    for a_tag in a_tags:
        rgx_group = re.search(rgx_pattern, a_tag['href'])
        station_name = rgx_group.group(1).replace('(', '_').replace(')', '')
        station_code = rgx_group.group(2)

        stations.update({
            station_name: station_code
        })

    return stations

