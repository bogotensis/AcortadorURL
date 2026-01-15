# Acortador de URLs con Analíticas

Este repositorio contiene el proyecto "Acortador de URLs con Analíticas", una aplicación que permite a los usuarios generar versiones cortas de URLs largas y, en futuras versiones, proporcionará estadísticas detalladas sobre su uso.

## Descripción del Proyecto

El objetivo principal de este proyecto es implementar un servicio robusto y escalable para acortar URLs. Las funcionalidades actuales incluyen:

*   **Acortamiento de URLs:** Permite a los usuarios enviar una URL larga y recibir a cambio una URL corta y única.
*   **Redirección:** Cuando un usuario accede a una URL corta, el servicio lo redirige automáticamente a la URL larga original.

## Stack Tecnológico

*   **Lenguaje:** Python
*   **Framework de API:** FastAPI
*   **Base de Datos:** SQLite (para desarrollo local)
*   **Framework de Pruebas:** Pytest
*   **Gestor de Tareas:** Makefile
*   **Integración Continua:** GitHub Actions

---

## Guía de Inicio Rápido

### 1. Prerrequisitos

*   Python 3.10+
*   `pip`

### 2. Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/bogotensis/AcortadorURL.git
    cd AcortadorURL
    ```

2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    make install
    ```

### 3. Ejecución Local

Para iniciar el servidor de desarrollo, ejecuta:

```bash
make run
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

*   La salida del servidor se guardará en el archivo `uvicorn.log`.
*   El proceso se ejecuta en segundo plano. Para detenerlo, puedes usar el comando `pkill uvicorn`.

### 4. Ejecutar los Tests

Para asegurarte de que todo funciona correctamente, puedes ejecutar la suite de pruebas:

```bash
make test
```

---

## API

La documentación interactiva de la API está disponible en la ruta `/docs` mientras la aplicación se está ejecutando:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Endpoints

#### `POST /shorten`

Acorta una nueva URL.

*   **Request Body:**
    ```json
    {
      "original_url": "https://ejemplo.com/mi/url/super/larga"
    }
    ```

*   **Ejemplo con `curl`:**
    ```bash
    curl -X POST -H "Content-Type: application/json" \
      -d '{"original_url": "https://ejemplo.com/mi/url/super/larga"}' \
      http://127.0.0.1:8000/shorten
    ```

*   **Respuesta Exitosa (201):**
    ```json
    {
      "short_url": "http://127.0.0.1:8000/XXXXXX"
    }
    ```

#### `GET /{short_code}`

Redirige a la URL original.

*   **Ejemplo con `curl` (usando el flag `-L` para seguir la redirección):**
    ```bash
    curl -L http://127.0.0.1:8000/XXXXXX
    ```