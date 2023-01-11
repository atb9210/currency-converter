import requests
import json
import pandas as pd
import csv

from_currency = str(
    input("Enter from currency: ").upper())

to_currency = str(
    input("Enter to currency: ").upper())

amount = float(input("Enter amount: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

#Carichiamo la risposta come testo
data = json.loads(response.text)

#Estrai oggetto contente oggeto con i valore di conversione e valuta
conversion_object = data['rates']

#Estrai solo il valore di conversione e valuta
conversion_value = float(conversion_object[to_currency])

print(data)

print(conversion_object)

print(conversion_value)

#print(response.status_code) 

#Esportiamo la risposta come testo leggibile con il valore di conversione e valuta
results_export= "I dati della conversione è di " + str(conversion_value) + " " + to_currency  + " da " + str(amount) + " " + from_currency 
print(results_export)

#stampiamo la risposta come testo leggibile con il valore di conversione in csv
f = open('results.csv','w')
f.write(results_export) 
f.close()
