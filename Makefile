# Makefile

# Instala las dependencias de Python
install:
	pip install -r requirements.txt

# Corre los tests
test:
	pytest

# Ejecuta la aplicación en modo de desarrollo
run:
	nohup uvicorn acortadorurl.main:app --host 0.0.0.0 > uvicorn.log 2>&1 &
