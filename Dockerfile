# 1. Imagen base
FROM python:3.11-slim

# 2. Crear un usuario no-root y directorio de trabajo
ENV HOME=/home/app
RUN useradd --create-home --home-dir $HOME app && \
    chown -R app:app $HOME
WORKDIR $HOME
USER app

# 3. Copiar e instalar dependencias para aprovechar la caché de Docker
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copiar el archivo .env
COPY --chown=app:app .env .

# 4. Copiar el código de la aplicación
COPY --chown=app:app acortadorurl/ ./acortadorurl/

# 5. Exponer el puerto y ejecutar la aplicación
EXPOSE 8000
CMD ["/home/app/.local/bin/uvicorn", "acortadorurl.main:app", "--host", "0.0.0.0", "--port", "8000"]