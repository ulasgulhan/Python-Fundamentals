from fastapi import FastAPI
from settings import engine
import models
from routers import category


app = FastAPI()

# FastAPI'da migration işlemini gerçekleştirmek için django'da olduğu gibi terminale özel shell kodları yazmıyoruz. Tek yapmamız gereken terminalde 'main.py' dosyasını yürütmek ve 'uvicorn main:app --reload' demek olacak. Aşağıdaki kod vasıtasıyla model içerisindeki sınıfları göçe hazırlıyoruz.
models.Base.metadata.create_all(bind=engine)


# routers klasörü altında açtığımız ".py" uzantılı dosyalarımızı buraya register ediyoruz ki proje ayağa kalktığında ilgili dosyalarda bulunan fonksiyonlar devreye girsin.
app.include_router(category.router)

