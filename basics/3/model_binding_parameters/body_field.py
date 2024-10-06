from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

# FastAPI sınıfının bir örneğini oluştur
app = FastAPI()

# Item modelini Pydantic kullanarak tanımla
class Item(BaseModel):
    name: str = Field(..., description="The name of the item")  # Gereken alan: Ürünün adı, bir string olmalı ve açıklama eklenmiş
    description: str | None = Field(
        default=None,                # Varsayılan değer: None
        title="The description of the item",  # Açıklama başlığı
        max_length=300               # Maksimum uzunluk: 300 karakter
    )
    price: float = Field(
        gt=0,                        # Fiyatın sıfırdan büyük olması gerekiyor
        description="The price must be greater than zero"  # Fiyat açıklaması
    )
    tax: float | None = None         # İsteğe bağlı alan: Vergi, varsayılan olarak None

# PUT isteği ile bir ürünü güncellemek için bir endpoint tanımla
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """
    Verilen item_id'ye göre bir ürünü güncelle.

    - `item_id`: Yolu parametresi (gerekli), güncellenecek ürünün ID'si.
    - `item`: Gövde parametresi (gerekli), yeni verilerle bir Item model örneği.
    
    JSON formatında bir yanıt döner ve `item_id` ile `item` içerir.
    """
    # Ürün ID'si ve ürün verilerini içeren bir sözlük oluştur
    results = {"item_id": item_id, "item": item}
    
    # Sonuçlar sözlüğünü JSON yanıt olarak döndür
    return results

