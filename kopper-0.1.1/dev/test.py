from writer import write_enum_class
from parser import parsing_raw_stations_info
from crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler()
    dict_info = {}

    for i in range(14):
        code, html = crawler.stations_by_korean_idx(i)
        with open("{}.html".format(i), 'w') as f:
            f.write(html)

        dict_info.update(
            parsing_raw_stations_info(html)
        )

    write_enum_class("dev-stations.py", "STATIONS", dict_info)
    