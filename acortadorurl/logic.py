# acortadorurl/logic.py
import string
import random

# "Base de datos" en memoria para almacenar las URLs
url_db = {}
# Usaremos un conjunto para verificar rápidamente la unicidad de los códigos cortos
used_short_codes = set()

def generate_short_code(length: int = 6) -> str:
    """
    Genera un código corto único y aleatorio.
    """
    characters = string.ascii_letters + string.digits
    while True:
        short_code = "".join(random.choice(characters) for _ in range(length))
        if short_code not in used_short_codes:
            used_short_codes.add(short_code)
            return short_code

def shorten_url(original_url: str) -> str:
    """
    Acorta una URL y la almacena en la base de datos.
    Devuelve el código corto.
    """
    # Por simplicidad, no verificamos si la URL ya existe.
    # En una aplicación real, lo haríamos para reutilizar códigos.
    short_code = generate_short_code()
    url_db[short_code] = original_url
    return short_code

def get_original_url(short_code: str) -> str | None:
    """
    Obtiene la URL original a partir de un código corto.
    """
    return url_db.get(short_code)