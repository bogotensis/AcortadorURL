# Hito 3: Diseño de Microservicios

Este documento detalla el diseño e implementación del primer microservicio para el proyecto "Acortador de URLs con Analíticas", cumpliendo con los requisitos del Hito 3.

## 1. Justificación del Framework

-   **Framework:** Se ha utilizado **FastAPI** para la construcción del microservicio.
-   **Justificación:** FastAPI es un framework web moderno y de alto rendimiento para Python. Su elección se basa en varias ventajas clave:
    -   **Rendimiento:** Es uno de los frameworks de Python más rápidos, comparable a NodeJS y Go, gracias a su base en Starlette (para la parte web) y Pydantic (para la validación de datos).
    -   **Facilidad de Uso y Desarrollo Rápido:** Su sintaxis es simple e intuitiva, lo que permite desarrollar APIs robustas con menos código.
    -   **Documentación Automática:** Genera automáticamente documentación interactiva de la API (usando Swagger UI y ReDoc), lo cual es fundamental para el diseño y prueba de las rutas.
    -   **Validación de Tipos:** Utiliza type hints de Python y Pydantic para una validación de datos robusta, reduciendo errores y mejorando la calidad del código.
    -   **Asincronía:** Soporta de forma nativa operaciones asíncronas, lo que es ideal para aplicaciones I/O bound como un servicio web que maneja muchas peticiones.

## 2. Diseño de la API y Separación de Lógica

Se ha diseñado la API siguiendo un enfoque de separación de capas para desacoplar la lógica de negocio de la capa de presentación (API).

-   **Capa de Lógica de Negocio (`acortadorurl/logic.py`):**
    -   Contiene las funciones puras que manejan la lógica del acortamiento: `generate_short_code`, `shorten_url`, y `get_original_url`.
    -   Gestiona el almacenamiento de datos (actualmente en memoria con un diccionario `url_db`).
    -   No tiene conocimiento del protocolo HTTP ni de FastAPI.

-   **Capa de API (`acortadorurl/main.py`):**
    -   Define la aplicación FastAPI y las rutas (endpoints).
    -   Maneja las peticiones y respuestas HTTP.
    -   Utiliza los modelos de Pydantic (`URLBase`, `URLShortened`) para la validación y serialización de datos.
    -   Llama a las funciones de la capa de lógica para realizar las operaciones.
    -   Implementa el logging de la actividad de la API.

### Rutas de la API

1.  **`POST /shorten`**
    -   **Descripción:** Recibe una URL larga y devuelve una versión corta.
    -   **Request Body:** `{"original_url": "string"}`
    -   **Response (201 Created):** `{"short_url": "string"}`
    -   **Lógica:** Valida la petición, llama a `logic.shorten_url`, construye la URL corta completa y la devuelve.

2.  **`GET /{short_code}`**
    -   **Descripción:** Redirige a la URL original correspondiente al código corto.
    -   **Path Parameter:** `short_code` (string)
    -   **Response (307 Temporary Redirect):** Redirige a la URL original.
    -   **Response (404 Not Found):** Si el `short_code` no existe.
    -   **Lógica:** Llama a `logic.get_original_url` y, si encuentra la URL, emite una respuesta de redirección.

## 3. Sistema de Logs

-   **Herramienta:** Se ha utilizado el módulo `logging` estándar de Python.
-   **Justificación:** Es una solución robusta, flexible y nativa de Python. No requiere dependencias externas y es altamente configurable para diferentes entornos (desarrollo, producción) y para enviar logs a diferentes destinos (consola, ficheros, servicios externos).
-   **Implementación:** Se ha configurado un logger básico en `acortadorurl/main.py` que registra en la consola (con nivel `INFO`) cada vez que se recibe una petición en las rutas de la API, proporcionando trazabilidad sobre la actividad del servicio.

## 4. Ejecución de Tests

-   Los tests de la API se encuentran en `tests/test_api.py`.
-   Se utiliza el `TestClient` de FastAPI para realizar peticiones HTTP al microservicio en un entorno de prueba, sin necesidad de levantar un servidor real.
-   Se comprueba el flujo completo de acortamiento y redirección, así como los casos de error como la no existencia de un código corto.
-   La correcta ejecución de los tests se verifica localmente con `make test` y automáticamente en el CI de GitHub Actions.
