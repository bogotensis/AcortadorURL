# tests/test_main.py

from acortadorurl.main import mi_primera_funcion

def test_mi_primera_funcion():
    """
    Esta prueba verifica que mi_primera_funcion devuelve True.
    """
    assert mi_primera_funcion() is True
