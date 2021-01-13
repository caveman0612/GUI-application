# from mysql import connector
import mysql.connector



def sendMysql(ticker, price):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="5359Root!@12",
        database="testdatabase"
    )
    mycursor = db.cursor()

    # mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

    mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", (ticker, price))
    db.commit()

    mycursor.execute("SELECT * FROM Person")

    for x in mycursor:
        print(x)





