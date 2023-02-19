import requests
import csv
from flask import Flask, render_template, request
app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('currencies.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=";") #changing ',' into ';'
    writer.writerow(data[0]['rates'][0].keys()) #keys meaning names of columns in csv
    for i in range(0, len(data[0]['rates'])): #no of elements meaning all rows
        writer.writerow(data[0]['rates'][i].values()) #values meaning inserting all rows to all columns 

#print(data[0]['rates'][0].get('ask')) as an example of selected ask-ratio on selected currency

@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == "POST":
#        print(request.form['currencies']) gives info on currency selected by user in form in currencies-calculator.html
#        print(request.form['quantity']) gives info on quantity of currency selected by user in form in currencies-calculator.html
        for i in range(0, len(data[0]['rates'])):
            if request.form["currencies"] == data[0]['rates'][i].get('code'): #checking which currency was selected
                price_result = float(request.form['quantity']) * float(data[0]['rates'][i].get('ask')) #multiplying quantity of selected currency by ask-ratio
                return "wynik obliczeń to: {}".format(price_result)
    else:
        return render_template("currencies-calculator.html")

if __name__=='__main__':
    app.run(debug=True)
