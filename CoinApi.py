import requests
import json
import sqlite3

currency = (input("currency to exchange to BTC: ")).upper()
url = f'https://rest.coinapi.io/v1/exchangerate/BTC/{currency}'
key = "FDB17D0D-3EA2-4E7D-8D07-5E20A75BFBC3"
headers = {'X-CoinAPI-Key': key}
response = requests.get(url, headers=headers)
# print(response.status_code)
# print(response.text)


# here we print requested currency info in a json format
result_json = response.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
# this prints all currency info in a json format
print(res_structured)

# here we only take the specific currency rate and print it out
rate = res["rate"]
print(f'1 BTC into {currency} is {rate} {currency}')


# this line of code saves the JSON in info.json file
with open('info.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)



time = res["src_side_base"][0]["time"]
asset = res["src_side_base"][0]["asset"]
rate = res["src_side_base"][0]["rate"]
volume = res["src_side_base"][0]["volume"]




# in this code we create a database
connection = sqlite3.connect('coinInfo.db')
cursor = connection.cursor()

# cursor.execute(""" CREATE TABLE coinINFO (
#             time VARCHAR(255) NOT NULL,
#             asset CHAR(25) NOT NULL,
#             rate INT,
#             volume INT
#             )""")


cursor.execute("""INSERT INTO coinINFO(time, asset, rate, volume) VALUES (?, ?, ?, ?)""", (time, asset, rate, volume))
connection.commit()

connection.close()

