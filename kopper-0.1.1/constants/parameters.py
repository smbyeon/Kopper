import enum

class PARAMETERS(enum.Enum):
    train_info = {
        'checkStnNm': 'Y',
        'chkCpn': 'N',
        'radJobId': '1',
        'SeandYo': 'N',
        'selGoDay': '',     # selected depart day (dd)
        'selGoHour': '',    # selected depart hour (HH)
        'selGoMonth': '',   # selected depart month (MM)
        'selGoSeat1': '015',
        'selGoTrain': '',   # train type code
        'selGoYear': '',    # selected depart year
        'start': '',        # selected depart date (yyyy.M.d)
        'txtGoAbrdDt': '', # selected depart date (yyyyMMdd)
        'txtGoEnd': '',     # arrival station name
        'txtGoHour': '',    # selected depart time (HHmmss)
        'txtGoPage': '1',
        'txtGoStart': '',   # department station name
        'txtGoYoil': '',    # selected a day of the week.
        'txtMenuId': '11',
        'txtPsgCnt1': '1',
        'txtPsgCnt2': '0',
        'txtPsgFlg_1': '1',
        'txtPsgFlg_2': '0',
        'txtPsgFlg_3': '0',
        'txtPsgFlg_4': '0',
        'txtPsgFlg_5': '0',
        'txtSeatAttCd_2': '000',
        'txtSeatAttCd_3': '000',
        'txtSeatAttCd_4': '015',
    }

    seat_info = {
        'arrSrcarNo': [1, 2, 3, 5, 6, 7, 8],
        'txtArvRsStnCd': '0020',
        'txtArvStnRunOrdr': '000024',
        'txtDptRsStnCd': '0001',
        'txtDptStnRunOrdr': '000001',
        'txtPsrmClCd': '1',
        'txtRunDt': '20170919',
        'txtSeatAttCd': '015',
        'txtSrcarCnt': '7',
        'txtSrcarNo': '1',
        'txtTotPsgCnt': '1',
        'txtTrnClsfCd': '02',
        'txtTrnGpCd': '102',
        'txtTrnNo': '01201',
    }

