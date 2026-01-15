from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
import string
import random

from .database import Base

class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
    short_code = Column(String, unique=True, index=True)

def create_db_tables(db_engine):
    Base.metadata.create_all(bind=db_engine)

def generate_short_code(db: Session, length: int = 6) -> str:
    """
    Genera un código corto único y aleatorio.
    """
    characters = string.ascii_letters + string.digits
    while True:
        short_code = "".join(random.choice(characters) for _ in range(length))
        # Verificar que el código corto no exista en la base de datos
        if not db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first():
            return short_code

def shorten_url(db: Session, original_url: str) -> str:
    """
    Acorta una URL y la almacena en la base de datos.
    Devuelve el código corto.
    """
    # Verificar si la URL original ya ha sido acortada
    db_url = db.query(ShortenedURL).filter(ShortenedURL.original_url == original_url).first()
    if db_url:
        return db_url.short_code

    short_code = generate_short_code(db)
    db_url = ShortenedURL(original_url=original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url.short_code

def get_original_url(db: Session, short_code: str) -> str | None:
    """
    Obtiene la URL original a partir de un código corto.
    """
    db_url = db.query(ShortenedURL).filter(ShortenedURL.short_code == short_code).first()
    return db_url.original_url if db_url else None
