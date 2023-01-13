import requests
import json
import csv
from conversione import *
import sqlite3
import datetime


conn = sqlite3.connect("logs.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_currency TEXT NOT NULL, 
    from_value INTEGER NOT NULL,
    to_currency TEXT NOT NULL,
    to_value INTEGER NOT NULL,
    date DATE NOT NULL)''')

conn.commit()

from_c = ""

while from_c != "stop":
    from_c = str(
        input("Enter from currency: ").upper())
        
    to_c = str(
        input("Enter to currency: ").upper())

    value = float(
        input("Enter amount: "))


    result = conv(from_c,to_c,value)
    date=datetime.date.today()

    print(result)


    #create logs database
    c.execute("INSERT INTO logs (from_currency, from_value,to_currency,to_value,date) VALUES (?,?,?,?,?)",(from_c,value,to_c,result,date))

    conn.commit()
conn.close()

#print(response.status_code) 

#Esportiamo la risposta come testo leggibile con il valore di conversione e valuta
# results_export= "I dati della conversione è di " + str(conversion_value) + " " + to_currency  + " da " + str(amount) + " " + from_currency 
# print(results_export)
