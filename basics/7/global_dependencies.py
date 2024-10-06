from fastapi import Depends, FastAPI, Header, HTTPException  # Gerekli FastAPI bileşenleri ve HTTPException'ı import eder
from typing_extensions import Annotated  # Annotated, tip açıklamaları için kullanılır

# X-Token başlığını doğrulayan bağımlılık fonksiyonu
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":  # Token doğru değilse
        raise HTTPException(status_code=400, detail="X-Token header invalid")  # 400 Hatalı İstek yanıtı döndürür

# X-Key başlığını doğrulayan bağımlılık fonksiyonu
async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":  # Key doğru değilse
        raise HTTPException(status_code=400, detail="X-Key header invalid")  # 400 Hatalı İstek yanıtı döndürür
    return x_key  # Doğru ise, x_key değerini döndürür

# FastAPI uygulaması oluşturulurken bağımlılıklar tanımlanır
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

# "/items/" yoluna yapılan GET isteğini karşılayan fonksiyon
@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]  # İstek başarılıysa, örnek veri döndürülür

# "/users/" yoluna yapılan GET isteğini karşılayan fonksiyon
@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]  # İstek başarılıysa, örnek kullanıcı verileri döndürülür
