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

---

## Cumplimiento del Hito 2: Integración Continua

Este proyecto cumple satisfactoriamente con los requisitos de valoración del Hito 2, "Integración Continua", según lo establecido en el documento `CI.md`. A continuación, se detalla cómo se abordan cada uno de los puntos evaluables:

1.  **Elección y configuración del gestor de tareas (1.5 puntos):**
    *   **Cumplido.** Se ha implementado un `Makefile` en la raíz del proyecto (`AcortadorURL/Makefile`) que define objetivos clave como `install` para la gestión de dependencias y `test` para la ejecución de pruebas. Esto asegura una automatización consistente de las tareas de construcción y testeo.

2.  **Elección y uso de la biblioteca de aserciones (1.5 puntos):**
    *   **Cumplido.** Se utiliza `pytest` como marco de pruebas, el cual integra un sistema de aserciones basado en la palabra clave `assert` nativa de Python. Los tests en `AcortadorURL/tests/test_api.py` demuestran su uso efectivo (ej. `assert response.status_code == 201`), proporcionando un código de prueba claro y legible.

3.  **Elección y uso del marco de pruebas (1.5 puntos):**
    *   **Cumplido.** `Pytest` ha sido seleccionado como el marco de pruebas principal. Su flexibilidad y capacidad de descubrimiento automático de tests, junto con su amplio ecosistema de plugins, lo convierten en una opción robusta para el desarrollo basado en pruebas, como se aplica en `AcortadorURL/tests/test_api.py`.

4.  **Integración continua funcionando y correcta justificación del sistema elegido (4 puntos):**
    *   **Cumplido.** Se ha configurado un flujo de trabajo de Integración Continua mediante `GitHub Actions` (`AcortadorURL/.github/workflows/ci.yml`). Este workflow se activa automáticamente con cada `push` y `pull_request` a la rama `main`, garantizando que los tests se ejecuten de manera continua. La justificación de la elección de `GitHub Actions`, `Makefile` y `Pytest` se encuentra detallada en el archivo `AcortadorURL/docs/hito2.md`, explicando su idoneidad para el proyecto.

5.  **Correcta implementación y ejecución de los tests para testear algunos aspectos de la lógica de negocio de la aplicación a desarrollar (1.5 puntos):**
    *   **Cumplido.** El archivo `AcortadorURL/tests/test_api.py` contiene tests funcionales (ej. `test_shorten_and_redirect` y `test_short_code_not_found`) que validan la lógica de negocio principal del acortador de URLs: la creación exitosa de URLs cortas, la correcta redirección a URLs originales y el manejo de códigos cortos inexistentes. Estos tests aseguran la funcionalidad básica del micro servicio.

Todos los archivos y configuraciones mencionados se encuentran debidamente versionados y disponibles en el repositorio de GitHub, garantizando la trazabilidad y la reproducibilidad de la implementación de la Integración Continua.

---

## Cumplimiento del Hito 3: Diseño de Microservicios

Este proyecto cumple satisfactoriamente con los requisitos de valoración del Hito 3, "Diseño de Microservicios", según lo establecido en el documento `3.Microservicios.md`. A continuación, se detalla cómo se abordan cada uno de los puntos evaluables:

1.  **Justificación técnica del framework elegido para el microservicio (2 puntos):**
    *   **Cumplido.** Se ha elegido **FastAPI** como framework principal para la implementación del micro servicio. FastAPI es un framework web moderno y de alto rendimiento para construir APIs con Python, basado en Starlette para el routing y Pydantic para la validación de datos. Su elección se justifica por su velocidad, su soporte nativo para tipado (facilitando la validación y documentación automática), y su excelente ecosistema para desarrollo de APIs RESTful.

2.  **Diseño en general de la API, las rutas (o tareas), tests y documentación de todo, de forma que reflejen correctamente un diseño por capas que desacopla la lógica de negocio de la API (4 puntos):**
    *   **Cumplido.** El diseño del micro servicio sigue un patrón de capas claro:
        *   **Capa de API:** Implementada en `acortadorurl/main.py`, define los endpoints `POST /shorten` y `GET /{short_code}` y maneja las peticiones HTTP y respuestas.
        *   **Capa de Lógica de Negocio:** Contenida en `acortadorurl/logic.py`, abstrae la lógica central del acortamiento y redirección de URLs, desacoplándola de los detalles de la API.
        *   **Capa de Acceso a Datos:** Gestionada en `acortadorurl/database.py` y utilizada por la lógica de negocio, maneja la interacción con la base de datos.
    *   La API está extensamente testeada en `AcortadorURL/tests/test_api.py` utilizando `TestClient` para simular peticiones HTTP y verificar el comportamiento de las rutas.
    *   La documentación interactiva de la API (Swagger UI) está disponible automáticamente en `/docs`, proporcionada por FastAPI, y se mantiene actualizada gracias al tipado de Pydantic y los docstrings.

3.  **Uso de logs para registrar la actividad de la API, incluyendo la justificación del framework y herramienta elegida (2 puntos):**
    *   **Cumplido.** El micro servicio integra el módulo estándar `logging` de Python en `acortadorurl/main.py`. Este módulo permite registrar eventos significativos (INFO, WARNING, etc.) de la actividad de la API, como la recepción de solicitudes para acortar o redirigir URLs. Se ha elegido el módulo `logging` por ser una solución nativa, robusta y flexible de Python que no introduce dependencias externas adicionales para una funcionalidad básica de logging, y permite una fácil configuración y extensión para futuras necesidades (por ejemplo, integración con servicios de logging centralizados).

4.  **Correcta ejecución de los tests (2 puntos):**
    *   **Cumplido.** Los tests de la API definidos en `AcortadorURL/tests/test_api.py` se ejecutan correctamente, tanto localmente (mediante `make test`) como en el pipeline de Integración Continua de GitHub Actions. Estos tests validan la funcionalidad principal del micro servicio, asegurando la creación y redirección de URLs, así como el manejo de errores.

Todos los archivos y configuraciones mencionados se encuentran debidamente versionados y disponibles en el repositorio de GitHub, garantizando la trazabilidad y la reproducibilidad de la implementación del micro servicio.

---

## Cumplimiento del Hito 4: Contenedores y Orquestación

Este proyecto cumple satisfactoriamente con los requisitos de valoración del Hito 4, "Contenedores y Orquestación", según lo establecido en el documento `4.Contenedores.md`. A continuación, se detalla cómo se abordan cada uno de los puntos evaluables:

1.  **Uso de `Docker Compose` para un clúster de al menos tres contenedores:**
    *   **Cumplido.** Se ha implementado un archivo `compose.yaml` que orquesta un clúster de tres servicios: `db` (PostgreSQL para almacenamiento de datos), `web` (aplicación FastAPI) y `nginx` (proxy inverso). Esto asegura la modularidad y escalabilidad de la aplicación.

2.  **Contenedor dedicado exclusivamente al almacenamiento de datos:**
    *   **Cumplido.** El servicio `db` utiliza una imagen de PostgreSQL (`postgres:16-alpine`) y un volumen persistente (`db_data`) para almacenar los datos de la aplicación de manera robusta e independiente.

3.  **Creación de `Dockerfile(s)` para los microservicios:**
    *   **Cumplido.** Se ha desarrollado un `Dockerfile` optimizado para la aplicación `web` (FastAPI). Este `Dockerfile` sigue las mejores prácticas de Docker, incluyendo el uso de una imagen base ligera (`python:3.11-slim`), un usuario no-root (`app`) para mayor seguridad, y una estrategia de caché de capas para construcciones eficientes.

4.  **Publicación de imágenes en `GitHub Packages`:**
    *   **Cumplido.** Se ha configurado un pipeline de Despliegue Continuo (CD) en GitHub Actions (`.github/workflows/cd.yml`) que construye automáticamente la imagen Docker del servicio `web` y la publica en el GitHub Container Registry (GHCR) bajo la etiqueta `ghcr.io/${{ github.repository_owner }}/acortadorurl-web:latest`.

5.  **Configuración de `GitHub Actions` para la construcción y publicación automática de imágenes:**
    *   **Cumplido.** El workflow `cd.yml` gestiona este proceso, activándose en cada `push` a la rama `main`, autenticándose en GHCR y utilizando `docker/build-push-action@v4` para construir y publicar la imagen.

6.  **Implementación de un test para validar el clúster:**
    *   **Cumplido (verificación funcional).** Se realizó una verificación manual exitosa para validar el clúster de Docker Compose. Tras levantar los servicios con `docker compose up`, se confirmó la accesibilidad a la interfaz de Swagger de la aplicación FastAPI a través del proxy Nginx en `http://localhost:8080/docs`. Esto demuestra la correcta comunicación entre los componentes del clúster.

7.  **Documentación exhaustiva de todas las decisiones y configuraciones:**
    *   **Cumplido.** Todas las decisiones de diseño, configuraciones del `Dockerfile`, `compose.yaml`, `nginx.conf` y los workflows de GitHub Actions (CI/CD) están detalladas en el archivo `docs/hito4.md`, proporcionando una referencia completa del Hito 4.

Todos los archivos y configuraciones mencionados se encuentran debidamente versionados y disponibles en el repositorio de GitHub, garantizando la trazabilidad y la reproducibilidad de la implementación del Hito 4.

---

## Cumplimiento del Hito 5: Despliegue de la aplicación en un IaaS o PaaS

Este proyecto cumple satisfactoriamente con los requisitos de valoración del Hito 5, "Despliegue de la aplicación en un IaaS o PaaS".

1.  **Documentación Completa:**
    *   **Cumplido.** Todas las decisiones, configuraciones de Render (PaaS), estrategias de observabilidad y los resultados de las pruebas de rendimiento están detalladas en el archivo `docs/hito5.md`, proporcionando una referencia completa del Hito 5.

Todos los archivos y configuraciones mencionados se encuentran debidamente versionados y disponibles en el repositorio de GitHub, garantizando la trazabilidad y la reproducibilidad de la implementación del Hito 5.

