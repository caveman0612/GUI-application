# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing
# second character of the final pair with an underscore ('_').


def solution(s):
    counter = 0
    answer = []
    temp_string = ""
    for letter in s:
        temp_string += letter
        counter += 1
        if counter % 2 == 0:
            answer.append(temp_string)
            temp_string = ""
    if len(s) % 2 != 0:
        answer.append(s[-1] + "_")
    print(answer)




solution("hello")