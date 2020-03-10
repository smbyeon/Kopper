from route import Route
from parser import parsing_raw_seat_info_by_srcar
def get_name_from_code(enum_cls, code):
    names_single = [name for name, member in enum_cls.__members__.items()
        if member.value == code]
    names_multiple = [name for name, member in enum_cls.__members__.items()
        if type(member.value) == tuple and code in member.value]

    # print(names_multiple, names_single)
    
    if not names_single and not names_multiple:
        raise ValueError("""Trains information is not enough.
            Please, add info(name, code) in 'enum/trains.py'.
            """)

    return names_single[0] if len(names_single) else names_multiple[0]


def get_routes(raw_train_routes):
    return [ Route(raw_route_info) for raw_route_info in raw_train_routes ]

