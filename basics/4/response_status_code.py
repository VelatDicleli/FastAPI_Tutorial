from fastapi import FastAPI  # Web uygulaması oluşturmak için FastAPI'yi import eder

app = FastAPI()  # FastAPI uygulamasının bir örneğini oluşturur

# Yeni bir öğe oluşturmak için endpoint'i tanımlar
@app.post("/items/", status_code=201)  # "/items/" adresinde POST isteği ile yanıt döner ve HTTP durum kodu 201 (Oluşturuldu) olarak ayarlanır
async def create_item(name: str):  # `name` parametresini alarak asenkron bir fonksiyon tanımlar
    return {"name": name}  # `name` parametresini içeren bir JSON yanıtı döner



from fastapi import FastAPI, status  # FastAPI'yi ve HTTP durum kodları için status'ü import eder
# Yeni bir öğe oluşturmak için endpoint'i tanımlar
@app.post("/items/", status_code=status.HTTP_201_CREATED)  # "/items/" adresinde POST isteği ile yanıt döner ve HTTP durum kodu 201 (Oluşturuldu) olarak ayarlanır
async def create_item(name: str):  # `name` parametresini alarak asenkron bir fonksiyon tanımlar
    return {"name": name}  # `name` parametresini içeren bir JSON yanıtı döner


# Yeni bir öğe oluşturmak için endpoint'i tanımlar
@app.post("/items/", status_code=status.HTTP_201_CREATED)  # "/items/" adresinde POST isteği ile yanıt döner ve HTTP durum kodu 201 (Oluşturuldu) olarak ayarlanır
async def create_item(name: str):  # `name` parametresini alarak asenkron bir fonksiyon tanımlar
    return {"name": name}  # `name` parametresini içeren bir JSON yanıtı döner
