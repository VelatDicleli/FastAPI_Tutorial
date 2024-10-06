from typing import Any  # Return türü olarak Any kullanımı için import edilir

from fastapi import FastAPI  # Web uygulaması oluşturmak için FastAPI'yi import eder
from pydantic import BaseModel, EmailStr  # Veri doğrulama için BaseModel ve e-posta doğrulama için EmailStr'yi import eder

app = FastAPI()  # FastAPI uygulamasının bir örneğini oluşturur

# Girdi doğrulama için veri modelini tanımlar
class UserIn(BaseModel):
    username: str  # Kullanıcı adı için gerekli alan
    password: str  # Şifre için gerekli alan
    email: EmailStr  # E-posta için gerekli alan, geçerli bir e-posta formatını doğrular
    full_name: str | None = None  # Tam ad için isteğe bağlı bir alan (varsayılan None)

# Çıktı temsili için veri modelini tanımlar
class UserOut(BaseModel):
    username: str  # Kullanıcı adı için gerekli alan
    email: EmailStr  # E-posta için gerekli alan
    full_name: str | None = None  # Tam ad için isteğe bağlı bir alan (varsayılan None)

# Yeni bir kullanıcı oluşturmak için endpoint'i tanımlar
@app.post("/user/", response_model=UserOut)  # "/user/" adresinde POST isteği ile yanıt modeli UserOut olarak tanımlanır
async def create_user(user: UserIn) -> Any:  # Kullanıcı oluşturma işlemini asenkron olarak gerçekleştiren fonksiyon
    return user  # Kullanıcı verilerini yanıt olarak döner
