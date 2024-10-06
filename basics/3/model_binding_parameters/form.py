from typing import Annotated  # Veri türlerini anotasyonlarla kullanmak için Annotated'ı import eder

from fastapi import FastAPI, Form  # FastAPI'yi ve form verileri için Form'u import eder

app = FastAPI()  # FastAPI uygulamasının bir örneğini oluşturur

# Kullanıcı giriş işlemini gerçekleştiren endpoint'i tanımlar
@app.post("/login/")  # "/login/" adresinde POST isteği ile yanıt döner
async def login(
    username: Annotated[str, Form()],  # `username` parametresini form verisi olarak alır
    password: Annotated[str, Form()]   # `password` parametresini form verisi olarak alır
):
    return {"username": username}  # Kullanıcı adını içeren bir JSON yanıtı döner
