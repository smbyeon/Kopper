import requests
import re

from bs4 import BeautifulSoup
from datetime import datetime

from group import *

class Korail:

    def __init__(self):
        self._trains = []

    def search_trains(self, depart="서울", arrive="부산", date=None, time=None, train_type="전체"):
        """
            date : "YYmmdd"
            time : "HHMMSS"
        """
        now = datetime.now()
        if date is None:
            date = now.strftime("%Y%m%d")
            day_code = now.strftime("%w")
        else:
            day_code = datetime.strptime(date, "%Y%m%d").strftime("%w")

        if time is None:
            time = now.strftime("%H%M%S")

        train_type = TRAIN_TYPE.NAME2CODE[train_type]
        
        _update = {
            "selGoTrain": train_type,
            "selGoTrainRa": train_type,
            "txtGoStart": depart,
            "txtGoEnd": arrive,
            "selGoYear": date[:4],
            "selGoMonth": date[4:6],
            "selGoDay": date[6:],
            "selGoHour": time[:2],
            "txtGoHour": time,
            "txtGoYoil": DAY.CODE2NAME[day_code],
            "txtGoAbrdDt": date
        }

        data = PARAM.SEARCH
        data.update(_update)

        r = requests.post(URL.SEARCH, data=data)
        soup = BeautifulSoup(r.text, "html5lib")

        scripts = soup.find_all("script", {"type": "text/javascript", "language": "javascripts"})

        for script in scripts:
            script = ''.join(script.text.split())
            info = re.search(PATTERN.SEARCH, script)
            info_dict = dict(zip(HEADER.SEARCH, info.group(1).replace('"', "").split(",")))

            self._trains.append(info_dict)

        import pprint
        pprint.pprint(self._trains)


    def search_seat(self, depart="서울", arrive="부산", date=None, time=None, train_type="무궁화호"):
        now = datetime.now()
        if date is None:
            date = now.strftime("%Y%m%d")
            day_code = now.strftime("%w")
        else:
            day_code = datetime.strptime(date, "%Y%m%d").strftime("%w")

        if time is None:
            time = now.strftime("%H%M%S")


        for info in self._trains:
            print(info["h_trn_clsf_cd"])
            if info["h_trn_clsf_cd"] == TRAIN_TYPE.NAME2CODE[train_type]:
                train_info = info
                print(info)
                break


        # 무궁화호 좌석 전체
        seat_list = [1, 2, 3, 5, 6, 7, 8]
        _update = {
            "txtSrcarCnt": len(seat_list),
            "arrSrcarNo": seat_list,
            "txtSrcarNo": 1, #2, 3, 4, 5, 6, 7
            "txtRunDt": train_info["h_run_dt"],
            "txtTrnClsfCd": train_info["h_trn_clsf_cd"],
            "txtTrnGpCd": train_info["h_trn_gp_cd"],
            "txtTrnNo": train_info["h_trn_no"],
            "txtSeatAttCd": train_info["h_seat_att_cd"],
            "txtDptRsStnCd": train_info["h_dpt_rs_stn_cd"],
            "txtArvRsStnCd": train_info["h_arv_rs_stn_cd"],
            "txtTotPsgCnt": "1",
            "txtDptStnRunOrdr": train_info["h_dpt_stn_run_ordr"],
            "txtArvStnRunOrdr": train_info["h_arv_stn_run_ordr"]
        }

        data = PARAM.SEAT
        data.update(_update)

        r = requests.post(URL.SEAT, data=data)
        soup = BeautifulSoup(r.text, "html5lib")

        div_seat = soup.find("div", {"class": "ck_seat"})
        div_room_num = div_seat.find("div", {"class": "tra_num"})
        room_num = div_room_num.text.strip()

        div_seat_offs = div_seat.find("div", {"class": "seat_box"}).find_all("span", {"class": "ck_seat_td2_off"})
        div_seat_ons = div_seat.find("div", {"class": "seat_box"}).find_all("span", {"class": "ck_seat_td2_on"})

        seat_offs = []
        for div_seat_off in div_seat_offs:
            seat_off = div_seat_off.text.strip()
            seat_offs.append(seat_off)


        seat_ons = []
        for div_seat_on in div_seat_ons:
            seat_on = div_seat_off.text.strip()
            seat_ons.append(seat_on)

        import pprint
        pprint.pprint(seat_ons)
        pprint.pprint(seat_offs)

if __name__ == "__main__":
    ko = Korail()
    ko.search_trains()
    ko.search_seat()