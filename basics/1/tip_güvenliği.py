
# FastAPI'de tip güvenliği için parametrelerin tipini yanına " : " işareti ile tanımlayabiliriz  " = " anlamına gelmez !.

def say_hi(name: str | None = None): # burada name parametresi string ya da None tipinde olabilir.
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
        
def process_items(items: list[str]): # items parametresi string türünde bir liste tipindedir.
    for item in items:
        print(item)
        

def process_items(prices: dict[str, float]): # prices parametresi bir sözlük tipindedir ve bu sözlük key : string , value : float tipindedir
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)