# acortadorurl/main.py
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import logic
from .database import get_db, engine

# --- Configuración de Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Lifespan Events ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear tablas en la base de datos al iniciar la aplicación
    logic.create_db_tables(engine)
    logger.info("Database tables created/checked.")
    yield
    # Limpieza al cerrar la aplicación (si es necesario)
    logger.info("Application shutting down.")

# --- Creación de la App FastAPI ---
app = FastAPI(
    title="Acortador de URLs",
    description="Un microservicio para acortar URLs y redirigir a las originales.",
    version="0.1.0",
    lifespan=lifespan,
)

# --- Configuración de CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todas las cabeceras
)

# --- Modelos de Datos (Pydantic) ---
class URLBase(BaseModel):
    original_url: str

class URLShortened(BaseModel):
    short_url: str

# --- Rutas de la API ---
@app.post("/shorten", response_model=URLShortened, status_code=201)
def create_short_url(url: URLBase, request: Request, db: Session = Depends(get_db)):
    """
    Recibe una URL original, genera un código corto único y lo guarda en la base de datos.

    - **URL original**: La URL que se desea acortar, enviada en el cuerpo de la solicitud.
    - **Respuesta exitosa (201)**: Devuelve la URL completa acortada, incluyendo el dominio.
    """
    original_url = url.original_url
    logger.info(f"Recibida solicitud para acortar URL: {original_url}")
    
    short_code = logic.shorten_url(db, original_url)
    
    # Construye la URL completa de respuesta
    base_url = str(request.base_url)
    short_url = f"{base_url}{short_code}"
    
    logger.info(f"URL acortada creada: {short_url}")
    return URLShortened(short_url=short_url)

@app.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    """
    Busca un código corto y redirige a la URL original correspondiente.

    - **Código corto**: El identificador único de la URL acortada.
    - **Redirección exitosa**: Responde con un HTTP 307 a la URL original.
    - **Error (404)**: Si el código corto no se encuentra en la base de datos.
    """
    logger.info(f"Recibida solicitud de redirección para el código: {short_code}")
    
    original_url = logic.get_original_url(db, short_code)
    
    if original_url is None:
        logger.warning(f"Código corto no encontrado: {short_code}")
        raise HTTPException(status_code=404, detail="URL corta no encontrada")
    
    logger.info(f"Redirigiendo a: {original_url}")
    return RedirectResponse(url=original_url)


