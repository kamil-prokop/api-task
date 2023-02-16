import requests, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('currencies.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(data[0]['rates'][0].keys()) #keys
    for i in range(0, len(data[0]['rates'])): #no of elements
        writer.writerow(data[0]['rates'][i].values()) #values
