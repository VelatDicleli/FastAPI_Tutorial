from fastapi import FastAPI  # FastAPI kütüphanesini içe aktarırız.

app = FastAPI()  # FastAPI uygulaması oluştururuz.

@app.get("/")  # Bu dekoratör, "/" yoluna GET isteği yapıldığında bu fonksiyonun çalışacağını belirtir (app.get() , app.post() etc.).
async def root():  # Asenkron olarak çalışan ve "root" adında bir fonksiyon tanımlarız.
    return {"message": "Hello World"}  # JSON formatında {"message": "Hello World"} döner.


# uygulamamızı ayağa kaldırmak için " fastapi dev merhaba_fastapi.py  "  komutunu cmd'ye gireriz.