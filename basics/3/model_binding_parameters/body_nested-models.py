# FastAPI kütüphanesinden FastAPI sınıfını ve Pydantic kütüphanesinden BaseModel sınıfını içe aktarır.
from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI uygulamasını başlatır.
app = FastAPI()

# 'Image' adında bir Pydantic modeli tanımlar.
# Bu model, bir resim için gerekli bilgileri içerir: URL ve isim.
class Image(BaseModel):
    url: str  # Resmin URL'sini temsil eder.
    name: str  # Resmin adını temsil eder.

# 'Item' adında bir Pydantic modeli tanımlar.
# Bu model, bir ürünü temsil eder ve bazı özellikleri içerir.
class Item(BaseModel):
    name: str  # Ürünün adını temsil eder.
    description: str | None = None  # Ürünün açıklamasını temsil eder (isteğe bağlı).
    price: float  # Ürünün fiyatını temsil eder.
    tax: float | None = None  # Ürünün vergisini temsil eder (isteğe bağlı).
    tags: set[str] = set()  # Ürüne ait etiketleri temsil eder (varsayılan olarak boş bir küme).
    image: Image | None = None  # Ürüne ait bir resmi temsil eder (isteğe bağlı).

# '/items/{item_id}' endpoint'ini tanımlar ve HTTP PUT isteği alır.
# Bu endpoint, bir ürünün güncellenmesini sağlar.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # 'item_id' ve 'item' bilgilerini içeren bir sonuç sözlüğü oluşturur.
    results = {"item_id": item_id, "item": item}
    # Sonuçları JSON formatında döner.
    return results
