def reverse_int(integer):
    result = 0
    negative = integer < 0
    integer = abs(integer)
    while integer != 0:
        result = result * 10 + integer % 10
        integer = integer / 10
    return -1 * result if negative else result
