# Makefile

# Instala las dependencias de Python
install:
	pip install -r requirements.txt

# Corre los tests
test:
	pytest
