# Makefile

# Instala las dependencias de Python
install:
	pip install -r requirements.txt

# Corre los tests
test:
	pytest

# Ejecuta la aplicación en modo de desarrollo
run:
	uvicorn acortadorurl.main:app --reload
