# https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

'''
              ---------------------------------------------------------------------------------
              |      srcar. 1     |      srcar. 2     |      srcar. 3     |      srcar. 4     |
              ---------------------------------------------------------------------------------
  route. 1    | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D |
              ---------------------------------------------------------------------------------
  route. 2    | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D |
              ---------------------------------------------------------------------------------
  route. 3    | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D |
              ---------------------------------------------------------------------------------
  route. 4    | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D | 1A | 1B | 1C | 1D |
              ---------------------------------------------------------------------------------
'''

def make_graph(parsed_seats_info):
    graph = []

    for route, seats_info in parsed_seats_info.items():
        srcar_nums = list(seats_info.keys())
        srcar_nums.sort(key=natural_keys)
        
        row = []
        for srcar_no in srcar_nums:
            seats_nums = list(seats_info[srcar_no].keys())
            seats_nums.sort(key=natural_keys)
            
            for seat_no in seats_nums:
                row.append(seats_info[srcar_no][seat_no])
            
        graph.append(row)

    return graph