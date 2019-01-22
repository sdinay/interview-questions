INT_MAX = 2**31 - 1
INT_MIN = -2**31

def reverse_int(integer):
    result = 0
    negative = integer < 0
    integer = abs(integer)
    print("Integer:", integer)
    while integer != 0:
        if (result > INT_MAX/10 or (result == INT_MAX/10 and integer % 10 > 7)):
            return 0
        if (result < INT_MIN/10 or (result == INT_MIN/10 and pop < -8)):
            return 0
        result = result * 10 + integer % 10
        print("Result:", result)
        integer = integer / 10
        print("Integer:", integer)
    return -1 * result if negative else result
