from fastapi import APIRouter, Depends, status, HTTPException, Path
from settings import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from models import Category


# buraya yarattığımız router nesnesi ile uygulamaya gelen request'leri ilgili fonksiyonlara ileteceğiz.
router = APIRouter()


# database ile bağlantımızı açıyoruz. Bağlantı açılırken bir hata olsa da olmasa da nesne ile işimiz bittiğinde bağlantıyı kapatıyoruz. Bu yüzden finally kullandık.
def get_db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Yukarıda kullandığımız yield terimi ilgili objeyi yani 'db' önceliğini belirtmek içindir. Yani yiedl ifadesinden sonra gelen kodun response dönüldükten sonra execute edilir. Bunu yapmamızdaki sebep uygulamamızın daha hızlı çalışmasını temin etmektir. Çünkü veritabanından bilgi alıp ön tarafa getirirken bize performans gerekir. Asenkron programlama ile aynı mantığı burada düşünebiliriz. İşlem bittikten sonra bir başka değişle execute end olduktan sonra bağlantı her zaman kapatılacaktır. Yaratılan 'db' nesnesi GC RAM'in heap alanından uçurulacaktır. Bu da her talep başına bir veritabanı bağlantısı yaratılacağı anlamınıa gelmektedir. Bunun tam tersi mantık ise singelton desing pattern'dir. Singleton ile nesne bir kez yaratılır ve proje koştukça aynı nesne kullanılır. Bunun kendine has sıkıntıları bulunmaktadır.


# Dependency Injection Principle uygulamak için aşağıdaki kodu kullandık. (Inversion of control'de dahil edeceğiz)
db_dependency = Annotated[Session, Depends(get_db_conn)]


# DTO (Data Transfer Object), UI (User Interface) yani arayüzden API'ye gelen verileri transfer etmek ilgili fonksiyonlara taşımak için kullanacağız. DTO'lar çift yönlü olarak çalıştırılabilinirler yani database'den çekilen data UI taşınırken de kullanılabilinir. UI'dan data taşımak için de kullanılabiliriz.
class CategoryDTO(BaseModel):
    name: str
    description: str = Field(min_length=2, max_length=100)


@router.post(path='/category/create', status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category_dto: CategoryDTO):
    model = Category()

    model.name = category_dto.name
    model.description = category_dto.description
    model.is_active = True

    db.add(model)
    db.commit()

    return {
        'status_code': 201,
        'transaction': 'Successful'
    }


@router.get(path='/', status_code=status.HTTP_200_OK)
async def get_all_categories(db: db_dependency):
    data = db.query(Category).all()

    if data is not None:
        return data

    raise HTTPException(
        status_code=404,
        detail='There is no data'
    )


@router.get(path='/category/{category_id}', status_code=status.HTTP_200_OK)
async def get_category_by_id(db: db_dependency, category_id: int = Path(gt=0)):
    data = db.query(Category).filter(Category.id == category_id).first()

    if data is not None:
        return data

    raise HTTPException(
        status_code=404,
        detail='Category not found'
    )


# Update operasyonu için iki tane yapımız bulunmaktadır. Bunlar put ve patch dir. Put bütün bir entity güncellemek için kullanılırken patch ilgili objenin belirli bir alanını güncellemeye yarar.
@router.put(path='/category/{category_id}', status_code=status.HTTP_200_OK)
async def update_category(db: db_dependency, category_dto: CategoryDTO, category_id: int = Path(gt=0)):
    data = db.query(Category).filter(Category.id == category_id).first()

    if data is None:
        raise HTTPException(
            status_code=404,
            detail='Category not found'
        )

    if db is None:
        raise HTTPException(
            status_code=500,
            detail='Database is cannot be reach'
        )

    data.name = category_dto.name
    data.description = category_dto.description

    db.add(data)
    db.commit()

    return {
        'status_code': 200,
        'transaction': 'Successful'
    }


@router.delete(path='/category/{category_id}', status_code=status.HTTP_200_OK)
async def delete_category(db: db_dependency, category_id: int = Path(gt=0)):
    data = db.query(Category).filter(Category.id == category_id).first()

    if data is None:
        raise HTTPException(
            status_code=404,
            detail='Category not found'
        )

    db.query(Category).filter(Category.id == category_id).delete()
    db.commit()

    return {
        'status_code': 200,
        'transaction': 'Successful'
    }


