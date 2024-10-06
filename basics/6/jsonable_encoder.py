from datetime import datetime  # datetime modülünü import eder (tarih ve saat işlemleri için)
from fastapi import FastAPI  # FastAPI framework'ünü import eder
from fastapi.encoders import jsonable_encoder  # Pydantic modellerini JSON'a çevirmek için gerekli fonksiyonu import eder
from pydantic import BaseModel  # Pydantic'in temel model sınıfını import eder

fake_db = {}  # Boş bir sözlük, sahte veritabanı olarak kullanılır


# Pydantic modelini tanımlar
class Item(BaseModel):
    title: str  # Item başlığı (zorunlu alan)
    timestamp: datetime  # Zaman damgası (zorunlu alan)
    description: str | None = None  # Açıklama alanı (isteğe bağlı)


app = FastAPI()  # FastAPI uygulaması oluşturulur


# PUT isteği ile item güncelleme işlemi yapılır
@app.put("/items/{id}")  # "/items/{id}" adresine yapılan PUT isteğini karşılar
def update_item(id: str, item: Item):  # `id` ve `item` parametrelerini alır
    json_compatible_item_data = jsonable_encoder(item)  # Pydantic modelini JSON uyumlu hale getirir
    fake_db[id] = json_compatible_item_data  # Sahte veritabanına bu veriyi ekler/günceller
    """
    Genelde noSql veritabanları için kullanılır. 
    """