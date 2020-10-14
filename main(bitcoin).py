from tkinter import *
import requests
import json

pycrypto=Tk()
pycrypto.title("My crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

def font_color(amount):
    if amount>0:
        return "green"
    else:
        return "red"

def my_portfolio():

    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=1000&convert=USD&CMC_PRO_API_KEY=4d284c7c-947f-4a9f-8870-dfc343a74d7d")
    
    api=json.loads(api_request.content)
    
    # print(api)
    # usage of for loop
    #coins=["STX","BAND","ZEN","CHSB"]
    
    
    coins=[{
            "symbol":"BTC",
            "amount_owned":380,
            "price_per_coin":45
            },
            {
            "symbol":"BAND",
            "amount_owned":8,
            "price_per_coin":32
            },
            {
            "symbol":"ZEN",
            "amount_owned":20000,
            "price_per_coin":45
            },
            {
            "symbol":"CHSB",
            "amount_owned":35,
            "price_per_coin":6
            },
            {
            "symbol":"STX",
            "amount_owned":70,
            "price_per_coin":5}
           ]
    
    total_pl=0
    coin_row=1
    total_current_value=0
    for i in range(0, 100):
        for coin in coins:
            if api["data"][i]["symbol"]==coin["symbol"]:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pl_coin=pl_percoin*coin["amount_owned"]
                total_pl=total_pl+total_pl_coin
                total_current_value=total_current_value+current_value
                
                # print(api["data"][i]["name"]+"-"+)
                # print("Price-${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number of coin:",coin["amount_owned"])
                # print("Toatl amount paid-","{0:.2f}".format(total_paid))
                # print("Current value:","${0:.2f}".format(current_value))
                # print("profit and Loss Per Coin:","${0:.2f}".format(pl_percoin))
                # print("Toatal prfit and Loss with coin:","${0:.2f}".format(total_pl_coin))
                # print("--------------------------------")
                
                
                name=Label(pycrypto,text=api["data"][i]["symbol"], bg="#F3F4F6" ,fg="black" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                name.grid(row= coin_row,column=0 ,sticky=N+S+E+W)
                
                price=Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6" ,fg="black" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                price.grid(row= coin_row,column=1,sticky=N+S+E+W)
                
                no_coins=Label(pycrypto,text=coin["amount_owned"], bg="#F3F4F6" ,fg="black" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                no_coins.grid(row= coin_row,column=2 ,sticky=N+S+E+W)
                
                amount_paid=Label(pycrypto,text="${0:.2f}".format(total_paid), bg="#F3F4F6" ,fg="black" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                amount_paid.grid(row= coin_row,column=3 ,sticky=N+S+E+W)
                
                Current_val=Label(pycrypto,text="${0:.2f}".format(current_value), bg="#F3F4F6" ,fg=font_color(float("{0:.2f}".format(current_value))) ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                Current_val.grid(row= coin_row,column=4 ,sticky=N+S+E+W)
                
                Pl_coin=Label(pycrypto,text="${0:.2f}".format(pl_percoin), bg="#F3F4F6" ,fg=font_color(float("{0:.2f}".format(pl_percoin))) ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                Pl_coin.grid(row= coin_row,column=5 ,sticky=N+S+E+W)
                
                totalpl=Label(pycrypto,text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6" ,fg=font_color(float("{0:.2f}".format(total_pl_coin))) ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
                totalpl.grid(row= coin_row,column=6 ,sticky=N+S+E+W)
                
               
        
                coin_row= coin_row+1
                
               
                
                #place outsite the increament value
              
    
    
        
    
    
           # print("total profit and loss for portfolia:",total_pl)
    total_pl=Label(pycrypto,text="${0:.2f}".format(total_pl), bg="#F3F4F6" ,fg=font_color(float("{0:.2f}".format(total_pl))) ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
    total_pl.grid(row= coin_row,column=6 ,sticky=N+S+E+W)
    total_plcv=Label(pycrypto,text="${0:.2f}".format(total_current_value), bg="#F3F4F6" ,fg="black" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
    total_plcv.grid(row= coin_row,column=4 ,sticky=N+S+E+W)
    
    api=""
    
    update=Button(pycrypto,text="Update", bg="#142E54" ,fg="white" ,command=my_portfolio, font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
    update.grid(row=coin_row+1,column=6 ,sticky=N+S+E+W)
                
    
    
    
    
    
    
name=Label(pycrypto,text="Coin name", bg="#142E54" ,fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
name.grid(row=0,column=0 ,sticky=N+S+E+W)

price=Label(pycrypto,text="Price", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
price.grid(row=0,column=1 ,sticky=N+S+E+W)

no_coins=Label(pycrypto,text="Coin Owned", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
no_coins.grid(row=0,column=2 ,sticky=N+S+E+W)

amount_paid=Label(pycrypto,text="Total Amount Paid", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
amount_paid.grid(row=0,column=3 ,sticky=N+S+E+W)

Current_val=Label(pycrypto,text="Current Value", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
Current_val.grid(row=0,column=4 ,sticky=N+S+E+W)

Pl_coin=Label(pycrypto,text="P/l Per Coin", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
Pl_coin.grid(row=0,column=5 ,sticky=N+S+E+W)

totalpl=Label(pycrypto,text="Total p/l with coin", bg="#142E54" ,fg="white" ,font="Lato 12 bold",padx="5",pady="5",borderwidth="0.5",relief="groove")
totalpl.grid(row=0,column=6 ,sticky=N+S+E+W)


my_portfolio()
pycrypto.mainloop()
print("Programm completed")

                
    
    
