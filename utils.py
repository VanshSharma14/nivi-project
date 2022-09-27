

def check_num(prev, cur, iteration):
    MULTIPLE = 300
    num = MULTIPLE * iteration
    
    # returns true if current number is closer
    if abs(prev-num) > abs(cur-num):
        return True
    # returns false if current number is further
    elif abs(prev-num) < abs(cur-num):
        return False
    # if they are equal returns true still [edge case]
    else: return True

def arr_index_finder(arr):
    # define arr of indecies that work
    indexArr = []
    # initialize basic values
    prev = None
    curr = arr[0]
    iteration = 1
    for i, el in enumerate(arr[1:], start=1):
        prev = curr
        curr = el
        if check_num(prev, curr, 1):
            print()