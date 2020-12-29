def validate_pin(pin):
    list = ["0","1","2","3","4","5","6","7","8","9"]
    counter = 0
    for i in pin:
        if i in list:
            counter += 1
        else:
            continue
    if counter == len(pin) and (counter == 4 or counter == 6):
        return True
        print("True")
    else:
        return False
        print("false")


validate_pin("1a1145")
validate_pin("1254")
validate_pin("121456")
validate_pin("-1234")
