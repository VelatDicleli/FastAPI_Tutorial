from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI sınıfının bir örneğini oluştur
app = FastAPI()

# Item modelini Pydantic kullanarak tanımla
class Item(BaseModel):
    name: str                        # Gereken alan: Ürünün adı, bir string olmalı
    description: str | None = None   # İsteğe bağlı alan: Ürünün açıklaması, sağlanmazsa varsayılan olarak None olur
    price: float                     # Gereken alan: Ürünün fiyatı, bir float olmalı
    tax: float | None = None         # İsteğe bağlı alan: Ürüne uygulanan vergi, sağlanmazsa varsayılan olarak None olur

# User modelini Pydantic kullanarak tanımla
class User(BaseModel):
    username: str                    # Gereken alan: Kullanıcının kullanıcı adı, bir string olmalı
    full_name: str | None = None     # İsteğe bağlı alan: Kullanıcının tam adı, sağlanmazsa varsayılan olarak None olur

# PUT isteği ile bir ürünü güncellemek için bir endpoint tanımla
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    """
    Verilen item_id'ye göre bir ürünü güncelle.

    - `item_id`: Yolu parametresi (gerekli), güncellenecek ürünün ID'si.
    - `item`: Gövde parametresi (gerekli), yeni verilerle bir Item model örneği.
    - `user`: Gövde parametresi (gerekli), kullanıcı bilgilerini içeren bir User model örneği.
    
    JSON formatında bir yanıt döner ve `item_id`, `item`, ve `user` içerir.
    """
    # Ürün ID'si, ürün verileri ve kullanıcı verilerini içeren bir sözlük oluştur
    results = {"item_id": item_id, "item": item, "user": user}
    
    # Sonuçlar sözlüğünü JSON yanıt olarak döndür
    return results
