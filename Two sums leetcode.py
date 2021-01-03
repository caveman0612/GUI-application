def twoSum(array, k):
    if len(array) < 2:
        return print("Too small of array")
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


twoSum([1,3,4,2,5,7,3,2,1,6,1], 7)

# checked = []
# answer = []
#
# for index, num in enumerate(nums):
#     inverse = target - num
#     if inverse not in checked:
#         checked.append[index] = num
#     else:


#
# """
# :type nums: List[int]
# :type target: int
# :rtype: List[int]
# """
