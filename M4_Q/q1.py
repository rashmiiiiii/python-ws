#single * for list
#duble ** for dictionary
'''1.	Write a program to read the stock_price.csv file and perform the following operations:
•	Convert Price to a numeric value (example: 1.02K = 1020)
•	Display the names of the two companies – one whose stock value is maximum and the other whose stock value is minimum.
•	Display the names of the companies whose stock value is within the price range that is input by the user.
'''
import csv
class Stock:
    def __init__(self,name,symbol,exchange,price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price
    def __str__(self):
        return f"{self.name} ,{self.symbol},{self.exchange},{self.price}"

def clean_init_get_stocks():
    stock_lst = []
    try:
        with open("stock_price.csv","r") as f:
            data = csv.reader(f,delimiter = ",")
            h = True
            for d in data:
                if h:
                    h = False
                    continue
                stock_lst.append(Stock(*d))
        for s in stock_lst:
            if "K" in s.price:
                s.price = float(s.price.strip().replace("K"," "))* 1000
            else:
                s.price = float(s.price.strip())
        
    except Exception as e:
        print('{},val {!r}.format(e.args[0],e)')
    return stock_lst
def show_stock_by_price(price):
    st_lst = clean_init_get_stocks()
    #logic find stock less tha n given price
    f = filter(lambda x:x.price <= price,st_lst)
    if f:
        show_stock_info(list(f))
    else:
        print("no stock find for given price:{price}")
def show_stock_info(lst):
    for s in lst:
        print(s)

def max_min_stock_price():
    st_lst = clean_init_get_stocks