# tests/test_api.py
from fastapi.testclient import TestClient
from acortadorurl.main import app

client = TestClient(app)

def test_shorten_and_redirect():
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

def test_short_code_not_found():
    """
    Prueba que se devuelve un 404 para un código corto que no existe.
    """
    response = client.get("/codigo_inexistente")
    assert response.status_code == 404
    assert response.json() == {"detail": "URL corta no encontrada"}