def solve(arr):
    arr.sort(reverse=True)
    new_arr = []
    new_arr.append(arr[0])
    counter = 0
    half_list = len(arr)
    for i in range(1, int(half_list)):
        if counter < half_list:
            new_arr.append(arr[-i])
            counter += 1
            if counter < half_list:
                new_arr.append(arr[i])
                counter += 1
            else:
                break
        else:
            break
    new_arr.pop(-1)
    return new_arr


solve([15, 11, 10, 7, 12])
solve([78,79,52,87,16,74,31,63,80])