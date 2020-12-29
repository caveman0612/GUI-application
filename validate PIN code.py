def validate_pin(pin):
    list = ["0","1","2","3","4","5","6","7","8","9"]
    counter = 0
    for i in pin:
        if i in list:
            counter += 1
        else:
            continue
    print(counter)
    print(len(pin))
    if counter == 4 or counter == 6 and counter == len(pin):
        # return True
        print("True")
    else:
        # return False
        print("false")


# validate_pin("1a1145")
# validate_pin("1254")
# validate_pin("12d456")
validate_pin("-1234")
