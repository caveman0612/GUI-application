# You are given two positive integer numbers a and b. These numbers are being simultaneously decreased by 1 until the
# # # smaller one is 0. Sometimes during this process the greater number is going to be divisible (as in with no remainder) by
# # # the smaller one. Your task is to tell how many times (starting with a and b) this will be the case.

def how_many_times(a, b):
    counter = 0
    list = [a, b]
    list.sort(reverse=True)
    a = list[0]
    print(a)
    b = list[1]
    print(b)
    while a > 0 and b > 0:
        if a % b == 0:
            counter += 1
            a += -1
            b += -1
        else:
            a += -1
            b += -1
    return counter



how_many_times(3, 5)
