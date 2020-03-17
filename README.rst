`Korail <http://www.letskorail.com/>`__ 에서 기차 예매를 진행할 때, 출발역에서 도착역까지 예매를 할 수 없는 경우
중간 정차역을 껴서 예매가 가능한 구간이 있는 지 확인하는 코드입니다.

+---------------+--------------------+------------------+--------------------+--------------------+
|               | :math:`Seat_{n-1}` | :math:`Seat_{n}` | :math:`Seat_{n+1}` | :math:`Seat_{n+k}` |
+===============+====================+==================+====================+====================+
| 서울-천안     | X                  | O                | X                  | X                  |
+---------------+--------------------+------------------+--------------------+--------------------+
| 천안-부산     | X                  | X                | O                  | X                  |
+---------------+--------------------+------------------+--------------------+--------------------+

서울에서 부산까지 완전히 비어있는 좌석이 없으므로 예약할 수 없지만, (서울 - 천안),
(천안 - 부산) 구간에서 티켓을 구매할 수 있습니다.

--------------

0. 설치
+++++++++

.. code:: bash

    pip install kopper


1. 기차 정보 조회
+++++++++++++++++

.. code:: python

    from kopper import *

    kopper = Kopper()

    # 기차 기본 정보 (최대 10개 조회)
    trains_info = kopper.trains_info("20200315", "60000", STATIONS.광명, STATIONS.부산, TRAIN_TYPE.KTX)


    for train_info in trains_info:
        print(train_info)

    """
    No.00101     KTX     광명(053100) ------ 부산(075100)
    No.00103     KTX     광명(054600) ------ 부산(081700)
    No.00105     KTX     광명(061600) ------ 부산(083700)
    No.00201     KTX_산천      광명(062100) ------ 부산(085400)
    No.00107     KTX     광명(065100) ------ 부산(091600)
    No.00109     KTX     광명(071600) ------ 부산(094000)
    No.00111     KTX     광명(074600) ------ 부산(100200)
    No.00113     KTX     광명(080900) ------ 부산(100700)
    No.00115     KTX     광명(081700) ------ 부산(104300)
    No.00119     KTX_산천      광명(095100) ------ 부산(122400)
    """

2. 기차 시간표 조회
+++++++++++++++++++

.. code:: python

    # 기차 선택
    selected_train_info = trains_info[0]

    # 선택한 기차 시간표 조회
    selected_train_schedule = kopper.train_schedule(selected_train_info) 

    print(selected_train_schedule)

    """
    광명 (05:31) - 대전 (06:10) 
    대전 (06:12) - 동대구 (06:56) 
    동대구 (06:58) - 신경주 (07:15) 
    신경주 (07:16) - 울산_통도사 (07:27) 
    울산_통도사 (07:29) - 부산 (07:51)
    """

3. 선택한 기차 칸 번호 조회
+++++++++++++++++++++++++++

.. code:: python

    selected_train_srcar_length = kopper.train_srcar_length(selected_train_info)

    print(selected_train_srcar_length)

    """
    ['1', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '17', '18']
    """

4. 예매할 수 있는 구간 출력
+++++++++++++++++++++++++++

.. code:: python

    # 보통 약 10 ~ 20초 정도 크롤링 시간 소요
    dict_selected_train_seats = kopper.train_seats_by_schedule(selected_train_info, selected_train_schedule, selected_train_srcar_length)

    kopper.report_routes(selected_train_schedule, dict_selected_train_seats)

    """
    광명 (05:31) - 부산 (07:51)
    """

.. |#f03c15| image:: https://placehold.it/10/f03c15/000000?text=+
.. |#3333ff| image:: https://placehold.it/10/3333ff/000000?text=+
.. |#009900| image:: https://placehold.it/10/009900/000000?text=+
