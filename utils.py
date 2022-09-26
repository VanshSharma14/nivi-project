

def check_num(prev, cur, iteration):
    MULTIPLE = 300
    num = MULTIPLE * iteration
    
    if abs(prev-num) < abs(cur-num):
        return prev
    else:
        return num
