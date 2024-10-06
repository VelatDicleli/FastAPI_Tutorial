from typing import Annotated  # Annotated, tip açıklamaları için kullanılır
from fastapi import Depends, FastAPI  # Depends, bağımlılık enjeksiyonu için kullanılır, FastAPI ise framework'tür

app = FastAPI()  # FastAPI uygulaması oluşturulur

# Sahte bir veritabanı oluşturulur (list içinde sözlükler)
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Ortak sorgu parametrelerini temsil eden sınıf
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):  # Sorgu parametreleri varsayılan değerlere sahiptir
        self.q = q  # q parametresi isteğe bağlı
        self.skip = skip  # Kaç kayıt atlanacağı
        self.limit = limit  # Kaç kayıt alınacağı

# "/items/" yoluna yapılan GET isteğini karşılayan fonksiyon
@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):  # Depends ile bağımlılık enjeksiyonu yapılır
    response = {}  # Yanıt için boş bir sözlük oluşturulur
    if commons.q:  # Eğer q parametresi gönderilmişse
        response.update({"q": commons.q})  # Yanıta q parametresi eklenir
    items = fake_items_db[commons.skip : commons.skip + commons.limit]  # Veritabanından skip ve limit'e göre veriler alınır
    response.update({"items": items})  # Yanıta alınan veriler
