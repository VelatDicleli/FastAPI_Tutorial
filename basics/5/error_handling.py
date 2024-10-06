from fastapi import FastAPI, HTTPException  # FastAPI ve HTTPException sınıflarını import eder

app = FastAPI()  # FastAPI uygulamasının bir örneğini oluşturur

# Varsayılan örnek veriler içeren bir sözlük
items = {"foo": "The Foo Wrestlers"}  # `items` sözlüğü, anahtar-değer çifti olarak bir öğe içerir

# Belirli bir öğeyi sorgulamak için endpoint tanımı
@app.get("/items/{item_id}")  # "/items/{item_id}" adresinde GET isteği ile yanıt döner
async def read_item(item_id: str):  # `item_id` parametresi, URL'den alınan bir string olarak tanımlanır
    if item_id not in items:  # Eğer `item_id` `items` sözlüğünde yoksa
        raise HTTPException(status_code=404, detail="Item not found")  # 404 Hata yanıtı döner ve "Item not found" mesajı verir
    return {"item": items[item_id]}  # Eğer `item_id` mevcutsa, ilgili öğeyi döner





from fastapi import FastAPI, Request  # FastAPI ve Request sınıflarını import eder
from fastapi.responses import JSONResponse  # JSON formatında yanıt döndürmek için JSONResponse'u import eder

# Özel bir istisna sınıfı oluşturur
class UnicornException(Exception):  # UnicornException adında bir özel hata sınıfı tanımlanır
    def __init__(self, name: str):  # Sınıfın başlatıcısı, bir isim alır
        self.name = name  # Bu isim sınıfın name alanına atanır


app = FastAPI()  # FastAPI uygulamasının bir örneği oluşturulur

# UnicornException için özel bir hata yöneticisi tanımlanır
@app.exception_handler(UnicornException)  # UnicornException türündeki hataları yakalamak için bir hata yöneticisi tanımlanır
async def unicorn_exception_handler(request: Request, exc: UnicornException):  # Hata yöneticisi, istek ve yakalanan hata örneğini alır
    return JSONResponse(  # JSON yanıtı döndürülür
        status_code=418,  # HTTP durum kodu 418 (I'm a teapot) döner
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},  # Özel bir hata mesajı döner
    )

# Belirli bir unicorn ismine göre işlem yapan bir endpoint tanımlanır
@app.get("/unicorns/{name}")  # "/unicorns/{name}" adresine yapılan GET isteği ile yanıt döner
async def read_unicorn(name: str):  # `name` parametresi URL'den alınır
    if name == "yolo":  # Eğer unicorn ismi "yolo" ise
        raise UnicornException(name=name)  # UnicornException fırlatılır
    return {"unicorn_name": name}  # Aksi takdirde unicorn ismi döndürülür







from fastapi import FastAPI, HTTPException  # FastAPI ve HTTPException sınıflarını import eder
from fastapi.exceptions import RequestValidationError  # RequestValidationError'ı import eder (doğrulama hatası için)
from fastapi.responses import PlainTextResponse  # Düz metin yanıtı için PlainTextResponse'u import eder
from starlette.exceptions import HTTPException as StarletteHTTPException  # Starlette HTTPException sınıfını import eder

app = FastAPI()  # FastAPI uygulamasının bir örneği oluşturulur

# HTTPException için özel hata yöneticisi tanımlanır
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):  # HTTPException oluştuğunda bu fonksiyon çalışır
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)  # Hata mesajını ve durum kodunu düz metin olarak döner

# RequestValidationError için özel hata yöneticisi tanımlanır
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):  # Doğrulama hatası oluştuğunda bu fonksiyon çalışır
    return PlainTextResponse(str(exc), status_code=400)  # Hata mesajını 400 (Geçersiz İstek) durumu ile düz metin olarak döner

# Bir öğeyi ID'sine göre getiren bir endpoint tanımlanır
@app.get("/items/{item_id}")  # "/items/{item_id}" adresinde GET isteği yapılır
async def read_item(item_id: int):  # `item_id` parametresi tamsayı olarak alınır
    if item_id == 3:  # Eğer `item_id` 3 ise
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")  # 418 Hata durumu ve özel mesajla HTTPException fırlatılır
    return {"item_id": item_id}  # `item_id` 3 değilse, öğe ID'sini döner





from fastapi import FastAPI, HTTPException  # FastAPI ve HTTPException sınıflarını import eder
from fastapi.exception_handlers import (  # FastAPI'nin hazır hata yöneticilerini import eder
    http_exception_handler,  # HTTPException için hazır hata yöneticisi
    request_validation_exception_handler,  # RequestValidationError için hazır hata yöneticisi
)
from fastapi.exceptions import RequestValidationError  # Doğrulama hatası için RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException  # Starlette HTTPException sınıfı

app = FastAPI()  # FastAPI uygulamasının bir örneği oluşturulur

# HTTPException için özelleştirilmiş hata yöneticisi
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):  # HTTP hatası olduğunda bu fonksiyon çalışır
    print(f"OMG! An HTTP error!: {repr(exc)}")  # Hata ile ilgili mesajı sunucuda yazdırır
    return await http_exception_handler(request, exc)  # Hazır http_exception_handler fonksiyonunu kullanarak yanıt verir

# RequestValidationError için özelleştirilmiş hata yöneticisi
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):  # Doğrulama hatası olduğunda bu fonksiyon çalışır
    print(f"OMG! The client sent invalid data!: {exc}")  # Doğrulama hatasını sunucuda yazdırır
    return await request_validation_exception_handler(request, exc)  # Hazır request_validation_exception_handler fonksiyonunu kullanarak yanıt verir

# Bir öğeyi ID'sine göre getiren bir endpoint tanımlanır
@app.get("/items/{item_id}")  # "/items/{item_id}" adresine yapılan GET isteği ile çalışır
async def read_item(item_id: int):  # item_id bir tamsayı olarak alınır
    if item_id == 3:  # Eğer `item_id` 3 ise
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")  # HTTP 418 hatası fırlatılır
    return {"item_id": item_id}  # Aksi takdirde öğe ID'sini döndürür
