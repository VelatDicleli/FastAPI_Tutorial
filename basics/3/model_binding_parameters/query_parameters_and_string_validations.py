from typing import Annotated  # Annotated, Python'un typing modülünden veri tiplerine ek açıklamalar eklememizi sağlar
from fastapi import FastAPI, Query ,Path # FastAPI ve Query parametresi içe aktarılıyor

app = FastAPI()  # FastAPI uygulaması başlatılıyor

# GET isteği için "/items/" yolunda bir endpoint tanımlıyoruz
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50, alias="item-query")] = None):  # Annotated ile q parametresini tip belirterek ve Query doğrulamasıyla işliyoruz
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}  # items isimli bir listeyi results'a ekliyoruz
    if q:  # Eğer q parametresi verilmişse
        results.update({"q": q})  # results sözlüğüne q parametresini de ekliyoruz
    return results  # results sözlüğünü JSON formatında geri döneriz

# "/items/" yoluna bir GET isteği yapıldığında çalışacak fonksiyonu tanımlıyoruz.
@app.get("/items/")
async def read_items(q: Annotated[str ,Query(min_length=3)] = ...):  # ... 3 nokta , zorunlu parametre geçişi anlamına gelir.
    """
    Bu fonksiyon, query parametresi olarak `q` alır ve min_length=3 kısıtlaması ile en az 3 karakter olmasını sağlar.
    """
    # Başlangıçta bir items listesi oluşturuyoruz.
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    
    # Eğer q parametresi verilmişse, bu parametre results'a eklenir.
    if q:
        results.update({"q": q})
        
    # results sözlüğünü JSON formatında döneriz.
    return results


@app.get("/items/{item_id}")  # Bu dekoratör, "/items/{item_id}" yoluna GET isteği yapıldığında bu fonksiyonun çalışacağını belirtir.
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],  # item_id bir path parametresi ve 0 ile 1000 arasında olmalı.
    q: str,  # q parametresi bir query parametresidir. (Kullanıcının URL'de '?q=something' şeklinde verdiği değer.)
    size: Annotated[float, Query(gt=0, lt=10.5)],  # size parametresi, 0'dan büyük ve 10.5'ten küçük bir float değer olmalı.
):
    results = {"item_id": item_id}  # İlk olarak, item_id'yi sonuçlarımıza ekliyoruz.
    if q:  # Eğer q parametresi verilmişse, sonuçlara q'yu ekliyoruz.
        results.update({"q": q})
    if size:  # Eğer size parametresi verilmişse, sonuçlara size'ı ekliyoruz.
        results.update({"size": size})
    return results  # Sonuçları JSON formatında geri döndürüyoruz.

