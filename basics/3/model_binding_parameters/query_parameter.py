from fastapi import FastAPI  # FastAPI kütüphanesini içe aktarırız

app = FastAPI()  # FastAPI uygulama nesnesini oluştururuz

# Sahte veri tabanı: item'lar listesi
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# İlk endpoint: "/items/" yoluna istek yaparak veritabanından item'lar alırız
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # skip ve limit varsayılan parametrelerle sayfalama yapar
    return fake_items_db[skip: skip + limit]  # skip'ten başlayarak limit kadar item döner

# İkinci endpoint: "/items/{item_id}" yoluna istek yaparak item ve needy parametrelerini alırız
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):  # item_id ve needy parametreleri alınıyor
    item = {"item_id": item_id, "needy": needy}  # Alınan değerlerle bir item oluşturulur
    return item  # Oluşturulan item JSON formatında döndürülür

# Test URL'leri:
# - http://127.0.0.1:8000/items/?skip=0&limit=10
# - http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
