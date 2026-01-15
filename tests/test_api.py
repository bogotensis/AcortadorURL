from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from acortadorurl.main import app
from acortadorurl.database import Base, get_db
from acortadorurl.logic import create_db_tables
import pytest

# --- Configuración de la Base de Datos de Prueba ---
# Usamos SQLite en memoria para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Crea un motor de base de datos específico para las pruebas
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Anula la dependencia get_db para las pruebas
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Cliente de pruebas para FastAPI
client = TestClient(app)

# Fixture para configurar y limpiar la base de datos antes y después de cada prueba
@pytest.fixture(name="session")
def session_fixture():
    # Asegúrate de que las tablas estén creadas para cada prueba
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    # Elimina todas las tablas después de cada prueba
    Base.metadata.drop_all(bind=engine)

def test_shorten_and_redirect(session):
    """
    Prueba el flujo completo: acortar una URL y luego ser redirigido.
    """
    original_url = "https://www.google.com"
    
    # 1. Acortar la URL
    response = client.post("/shorten", json={"original_url": original_url})
    assert response.status_code == 201
    
    data = response.json()
    assert "short_url" in data
    
    short_url = data["short_url"]
    # El código corto es la última parte de la URL
    short_code = short_url.split("/")[-1]
    
    # 2. Redirigir usando el código corto
    # allow_redirects=False para poder inspeccionar la respuesta de redirección
    response = client.get(f"/{short_code}", follow_redirects=False)
    
    # Debería ser una redirección 307 Temporal Redirect
    assert response.status_code == 307
    assert response.headers["location"] == original_url

def test_short_code_not_found(session):
    """
    Prueba que se devuelve un 404 para un código corto que no existe.
    """
    response = client.get("/codigo_inexistente")
    assert response.status_code == 404
    assert response.json() == {"detail": "URL corta no encontrada"}
