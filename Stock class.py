f= open("List of stocks.txt","a+")
f.write("appended line")

class stocks():

    def __init__(self, name, price):
        self.name = name
        self.price = price



f.close()