# from mysql import connector
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="5359Root!@12",
        database="testdatabase"
    )

def savedatatosql(name, ticker, TargetPrice):

    mycursor = db.cursor()

    # mycursor.execute("CREATE TABLE Companies (name VARCHAR(50), ticker TINYTEXT, TargetPrice mediumint UNSIGNED, CompanyID int PRIMARY KEY AUTO_INCREMENT)")
    # db.commit()

    mycursor.execute("INSERT INTO Companies (name, ticker, TargetPrice) VALUES (%s,%s,%s)", (name, ticker, TargetPrice))
    db.commit()

    # mycursor.execute("DELETE FROM companies WHERE name = 'tesla'")
    # db.commit()

def seemysqltables():

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM Companies")
    for x in mycursor:
        print(x)

seemysqltables()

def pulltickerandprices():
    mycursor = db.cursor()
    mycursor.execute("SELECT ticker, TargetPrice FROM Companies")

    myresults = mycursor.fetchall()
    return myresults
    # print(myresults)
    # for x in myresults:
    #     print(x)

# pulltickerandprices()