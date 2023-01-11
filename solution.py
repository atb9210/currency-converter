import requests
import json

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