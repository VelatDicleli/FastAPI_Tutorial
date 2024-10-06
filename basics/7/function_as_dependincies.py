from typing import Annotated  # Annotated, tip açıklamaları için kullanılır
from fastapi import Depends, FastAPI  # Depends, bağımlılık enjeksiyonu için kullanılır, FastAPI framework'tür

app = FastAPI()  # FastAPI uygulaması oluşturulur


# Ortak parametreleri alan bir bağımlılık fonksiyonu tanımlanır
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}  # Sorgu parametrelerini bir sözlük olarak döndürür


# "/items/" yoluna yapılan GET isteğini karşılayan fonksiyon
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):  # `common_parameters` fonksiyonuna bağımlıdır
    return commons  # Gelen parametreleri döndürür


# "/users/" yoluna yapılan GET isteğini karşılayan fonksiyon
@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):  # Aynı şekilde `common_parameters` fonksiyonuna bağımlıdır
    return commons  # Gelen parametreleri döndürür
