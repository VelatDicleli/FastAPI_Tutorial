from fastapi import FastAPI  # FastAPI framework'ünü içe aktarıyoruz
from pydantic import BaseModel  # Pydantic'in BaseModel sınıfını kullanarak veri doğrulaması yapıyoruz


# Item sınıfını oluşturuyoruz, bu sınıf Pydantic'in BaseModel sınıfından miras alır
class Item(BaseModel):
    name: str  # Zorunlu bir string alan
    description: str | None = None  # İsteğe bağlı bir string alan (None olabilir)
    price: float  # Zorunlu bir float (ondalıklı sayı) alan
    tax: float | None = None  # İsteğe bağlı bir float alan (None olabilir)


app = FastAPI()  # FastAPI uygulama nesnesi oluşturuyoruz


# POST isteği ile "/items/" yoluna bir yeni item ekleriz
@app.post("/items/")
async def create_item(item: Item):  # item: Item ile Pydantic veri doğrulamasını kullanıyoruz
    return item  # Gönderilen veriyi olduğu gibi geri döneriz


# PUT isteği ile "/items/{item_id}" yoluna istek yaparak mevcut bir item güncellenir
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):  # item_id, item ve isteğe bağlı q parametrelerini alırız
    result = {"item_id": item_id, **item.dict()}  # item_id'yi ve item verisini dict'e çevirerek sonucu döneriz
    if q:
        result.update({"q": q})  # Eğer q değeri varsa, bu değeri de sonuca ekleriz
    return result  # Sonucu JSON formatında döneriz


# Test URL'leri:
# 1. POST için: http://127.0.0.1:8000/items/
#    Body kısmına:
#    {
#       "name": "Laptop",
#       "description": "A powerful laptop",
#       "price": 1500.00,
#       "tax": 150.00
#    } gönderilir.
#
# 2. PUT için: http://127.0.0.1:8000/items/1?q=updated
#    Body kısmına:
#    {
#       "name": "Laptop",
#       "description": "Updated description",
#       "price": 1400.00,
#       "tax": 100.00
#    } gönderilir.
