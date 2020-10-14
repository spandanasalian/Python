from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My crypto portfolio")

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=9ea71a23-9490-4638-8c34-8a6c6c5d4413")
    api = json.loads(api_request.content)
    coins = [{"Symbol":"BTC","amount_owned":2,"price_per_coin":3200},{"Symbol":"ETH","amount_owned":100,"price_per_coin":2.055}]
    total_pl = 0
    coin_row = 0

    for i in range(0,5):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["Symbol"]:
                # total_amount_paid = coin["amount_owned"] * coin["price_per_coin"]
                # current_value = api["data"][i]["quote"]["USD"]["price"] * coin["amount_owned"]
                # pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                # total_pl_coin = pl_per_coin * coin["amount_owned"]
                # total_pl = total_pl + total_pl_coin
                
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pl_coin=pl_percoin*coin["amount_owned"]
                total_pl=total_pl + total_pl_coin
                
                #print(api["data"][i]["name"]," - ", api["data"][i]["symbol"] )
                #print("price - " ,"{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                #print("no. of coins owned - ",coin["amount_owned"])
                #print("total_amount_paid - ","${0:.2f}".format(total_amount_paid))
                #print('current value - ',"${0:.2f}".format(current_value))
                #print("pl_per_coin - " ,"${0:.2f}".format(pl_per_coin))
                #print("Total profit/loss from the portfolio - ","${0:.2f}".format(total_pl))

                coin_name = Label(pycrypto, text=api["data"][i]["symbol"], bg="white", fg="black")
                coin_name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                price = Label(pycrypto, text="{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="grey", fg="black")
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                no_of_coins = Label(pycrypto, text=coin["amount_owned"], bg="white", fg="black")
                no_of_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                total_amount = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="grey", fg="black")
                total_amount.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_value = Label(pycrypto, text="${0:.2f}".format(current_value), bg="white", fg="black")
                current_value.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_percoin), bg="grey", fg="black")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                total_pl = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="white", fg="grey")
                total_pl.grid(row=coin_row, column=6, sticky=N + S + E + W)
                coin_row = coin_row + 1



name = Label(pycrypto,text="coinname",bg="white",fg="black")
name.grid(row=0,column=0,sticky=N+S+E+W)

price = Label(pycrypto,text="price",bg="grey",fg="black")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_of_coins = Label(pycrypto,text="Coin owned",bg="white",fg="black")
no_of_coins.grid(row=0,column=2,sticky=N+S+E+W)

total_amount = Label(pycrypto,text="Total amount paid",bg="grey",fg="black")
total_amount.grid(row=0,column=3,sticky=N+S+E+W)

current_value = Label(pycrypto,text="Current value",bg="white",fg="black")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin = Label(pycrypto,text="P/L coin",bg="grey",fg="black")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl = Label(pycrypto,text="Total P/l",bg="white",fg="grey")
total_pl.grid(row=0,column=6,sticky=N+S+E+W)


my_portfolio()


pycrypto.mainloop()


print("program completed")