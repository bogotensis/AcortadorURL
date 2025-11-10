# acortadorurl/main.py
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from . import logic

# --- Configuración de Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Creación de la App FastAPI ---
app = FastAPI(
    title="Acortador de URLs",
    description="Un microservicio para acortar URLs y redirigir a las originales.",
    version="0.1.0",
)

# --- Modelos de Datos (Pydantic) ---
class URLBase(BaseModel):
    original_url: str

class URLShortened(BaseModel):
    short_url: str

# --- Rutas de la API ---
@app.post("/shorten", response_model=URLShortened, status_code=201)
def create_short_url(url: URLBase, request: Request):
    """
    Crea una URL corta a partir de una URL original.
    """
    original_url = url.original_url
    logger.info(f"Recibida solicitud para acortar URL: {original_url}")
    
    short_code = logic.shorten_url(original_url)
    
    # Construye la URL completa de respuesta
    base_url = str(request.base_url)
    short_url = f"{base_url}{short_code}"
    
    logger.info(f"URL acortada creada: {short_url}")
    return URLShortened(short_url=short_url)

@app.get("/{short_code}")
def redirect_to_original(short_code: str):
    """
    Redirige a la URL original a partir de un código corto.
    """
    logger.info(f"Recibida solicitud de redirección para el código: {short_code}")
    
    original_url = logic.get_original_url(short_code)
    
    if original_url is None:
        logger.warning(f"Código corto no encontrado: {short_code}")
        raise HTTPException(status_code=404, detail="URL corta no encontrada")
    
    logger.info(f"Redirigiendo a: {original_url}")
    return RedirectResponse(url=original_url)
