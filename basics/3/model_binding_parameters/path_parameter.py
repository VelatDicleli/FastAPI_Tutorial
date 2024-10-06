from fastapi import FastAPI  # FastAPI framework'ünü import ediyoruz

app = FastAPI()  # FastAPI uygulama nesnesini oluşturuyoruz


# İlk endpoint'imiz: item_id'yi URL'den alarak bir yanıt döner
@app.get("/items/{item_id}")  # GET isteğiyle "/items/{item_id}" yoluna istek yapılabilir
async def read_item(item_id: int):  # "item_id" parametresi bir tam sayı olmalı
    return {"item_id": item_id}  # JSON formatında "item_id" geri döner

# Enum sınıfı, önceden tanımlı modeller için sabitler oluşturur
from enum import Enum  # Enum kütüphanesini import ediyoruz

class ModelName(str, Enum):  # Enum sınıfını oluşturuyoruz ve bu sınıf "str" tabanlı
    alexnet = "alexnet"  
    resnet = "resnet"    
    lenet = "lenet"      

# İkinci endpoint'imiz: model_name'e göre farklı mesajlar döndürüyor
@app.get("/models/{model_name}")  # GET isteğiyle "/models/{model_name}" yoluna istek yapılabilir
async def get_model(model_name: ModelName):  # model_name parametresi ModelName enum'undaki bir değer olmalı
    if model_name is ModelName.alexnet:  # Eğer model_name "alexnet" ise
        return {"model_name": model_name, "message": "Deep Learning FTW!"}  # Bu mesajı geri döneriz

    if model_name.value == "lenet":  # Eğer model_name "lenet" ise
        return {"model_name": model_name, "message": "LeCNN all the images"}  # Bu mesajı geri döneriz

    return {"model_name": model_name, "message": "Have some residuals"}  # Diğer tüm durumlar için bu mesaj döner
