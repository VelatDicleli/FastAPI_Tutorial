from typing import Annotated  # Verileri anotasyonlarla tanımlamak için Annotated'ı import eder

from fastapi import FastAPI, File, UploadFile  # FastAPI'yi, dosya işlemleri için File ve UploadFile sınıflarını import eder

app = FastAPI()  # FastAPI uygulamasının bir örneğini oluşturur

# Dosya yüklemek için endpoint tanımı
@app.post("/files/")  # "/files/" adresinde POST isteği ile yanıt döner
async def create_file(file: Annotated[bytes, File()]):  # `file` parametresi bir dosya olarak alınır, bytes türünde işlenir
    return {"file_size": len(file)}  # Dosyanın boyutunu (byte cinsinden) döner

# Yüklenen dosyanın bilgilerini almak için endpoint tanımı
@app.post("/uploadfile/")  # "/uploadfile/" adresinde POST isteği ile yanıt döner
async def create_upload_file(file: UploadFile):  # `file` parametresi UploadFile türünde alınır
    return {"filename": file.filename}  # Yüklenen dosyanın adını döner






from fastapi.responses import HTMLResponse  # HTML yanıtları döndürmek için HTMLResponse import edilir

app = FastAPI()  # FastAPI uygulamasının bir örneği oluşturulur

# Birden fazla dosya yüklemek için endpoint tanımı
@app.post("/files/")  # "/files/" adresinde POST isteği ile yanıt döner
async def create_files(files: Annotated[list[bytes], File()]):  # `files` parametresi, bytes formatında bir liste olarak alınır
    return {"file_sizes": [len(file) for file in files]}  # Yüklenen her dosyanın boyutlarını (byte cinsinden) bir liste olarak döner

# Birden fazla dosya yüklemek ve dosya adlarını almak için endpoint tanımı
@app.post("/uploadfiles/")  # "/uploadfiles/" adresinde POST isteği ile yanıt döner
async def create_upload_files(files: list[UploadFile]):  # `files` parametresi UploadFile türünde bir liste olarak alınır
    return {"filenames": [file.filename for file in files]}  # Yüklenen dosyaların adlarını bir liste olarak döner

# Ana sayfa için basit bir HTML formu döner
@app.get("/")  # HTTP GET isteği ile "/" adresine istek yapılır
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">  # Dosyaları yüklemek için bir form
<input name="files" type="file" multiple>  # Birden fazla dosya seçmeye izin veren bir dosya girişi
<input type="submit">  # Formu göndermek için bir buton
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">  # Başka bir dosya yükleme formu
<input name="files" type="file" multiple>  # Birden fazla dosya seçmeye izin veren bir dosya girişi
<input type="submit">  # Formu göndermek için bir buton
</form>
</body>
    """
    return HTMLResponse(content=content)  # HTML içeriğini yanıt olarak döner
