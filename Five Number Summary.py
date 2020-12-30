# #Introduction For a given set of data, the five number summary can provide a quick sense of the location and spread of those observations. The five number summary consists of the following values (in order):
#
# Minimum
# First Quartile (Q1)
# Median (Second Quartile; Q2)
# Third Quartile (Q3)
# Maximum


def five_num(array):
    array.sort()
    minimum = min(array)
    first_qtr = 0
    med = 0
    third_qtr = 0
    maximum = max(array)

    if len(array) % 2 == 0:
        med_1_index = int((len(array)-1) / 2)
        med_2_index = int(len(array)/2)
        med_2 = array[int(len(array)/2)]
        med_1 = array[int((len(array)-1) / 2)]
        med = (med_1 + med_2)/2

        #deals with 1st and 3rd quartile oif array is even
        lower_list = array[:(med_1_index + 1)]
        upper_list = array[med_2_index:]
        first_qtr = lower_list[int((len(lower_list) - 1)/2)]
        third_qtr = upper_list[int((len(lower_list) - 1) / 2)]

    else:
        med = (len(array) - 1)

        lower_list = array[:int((len(array) + 1)/2)]
        upper_list = array[int(len(array) / 2):]
        first_qtr = lower_list[int((len(lower_list) - 1) / 2)]
        third_qtr = upper_list[int((len(lower_list) - 1) / 2)]

    number_summary = [minimum, first_qtr, med, third_qtr, maximum]
    return number_summary



five_num([4, 6, -6, 7, -3, 5, -2])
