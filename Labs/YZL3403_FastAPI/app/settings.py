from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# veritabanımızın lokasyonunu yani yolunu ilgili değişkene attık.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./api.db'

# SQLALCHEMY ORM aracının kullanan bir web app ile veritabanımızın nasıl konuşacağını configure ettiğimiz yapı aşağıdadır. Bu bağlantıyı kurmak için yukarıda import ettiğimiz create_engine sınıfından instance aldık.
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={
        'check_same_thread': False
    }
)

# sessionmaker() sınıfından aldığım instance vasıtasıyla veritabanında bir oturum oluşturacağız. Oluşturduğumuz bu oturumda CRUD operasyonlarından aktif olarak bu oturum üzerinden işlemleri yürüteceğiz.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# bind => yeni oluşturulan session nesnesi ile yukarıda yaratılan engine ilişkilendirmesini ya da bir başka değiş ile engin'de verilen yoldaki database bu ayarla bağlan
# autoflush => her yeni session nesnesini oluşturduğumuzda ayarları temizleme işlemi için kullanılır. Biz aynı auth bilgileri ile devam edeceğiz o yüzden false
# autocommit => SQLALCHEMY autocommit olmadan yani burada false dediğimizde session.commit() ve session.rollback() fonksiyonlarını çağırma ve işlemlerinin durumunu manuel olarak yönetmeyi sağlıyoruz.

# declarative_base() sınıfından instance alarak yarattığımız nesneyi model oluştururken faydalanacağız. Yani model yaratırken ihtiyaç duyulan özellikleri "Base" nesnemiz temin edecek
Base = declarative_base()
