# Hito 4: Contenedores y Orquestación

## Introducción

Este hito se enfoca en la contenerización de la aplicación "Acortador de URLs" y la orquestación de sus servicios utilizando Docker Compose. El objetivo es desplegar la aplicación en un clúster de contenedores que incluya la aplicación FastAPI, una base de datos PostgreSQL y un proxy inverso Nginx.

## Mejoras en el Dockerfile de la Aplicación

Para asegurar una contenerización eficiente y segura, se realizaron mejoras significativas en el `Dockerfile` de la aplicación `AcortadorURL`.

*   **Archivo `.dockerignore`:** Se creó para excluir archivos y directorios innecesarios del contexto de construcción de la imagen, reduciendo el tamaño final de la imagen y acelerando el proceso de construcción. Posteriormente, se **eliminó la entrada `.env`** de este archivo para permitir que el `Dockerfile` copiara el archivo de configuración de entorno al contenedor, resolviendo un error de construcción.
*   **Imagen Base Optimizada:** Se optó por `python:3.11-slim` como imagen base para reducir el tamaño de la imagen final.
*   **Usuario no-root:** Se configuró la ejecución de la aplicación dentro del contenedor con un usuario no-root (`app`) para mejorar la seguridad, siguiendo las mejores prácticas de Docker.
*   **Optimización de Caché:** El `Dockerfile` se estructuró para aprovechar la caché de capas de Docker, instalando las dependencias (`requirements.txt`) antes de copiar el código de la aplicación. Esto asegura que la reconstrucción de la imagen sea más rápida si solo cambia el código de la aplicación y no las dependencias.

## Configuración de la Base de Datos

La aplicación se adaptó para utilizar una base de datos PostgreSQL, en lugar de SQLite, para cumplir con los requisitos de un sistema de gestión de bases de datos robusto y adecuado para entornos de producción.

*   **`requirements.txt`:** Se añadió `psycopg2-binary` para permitir la conexión a bases de datos PostgreSQL desde Python y `python-dotenv` para la gestión de variables de entorno.
*   **`acortadorurl/database.py`:** Se verificó y confirmó que el archivo ya estaba configurado para leer la URL de conexión de la base de datos (DATABASE_URL) desde las variables de entorno, gracias a `pydantic-settings`. Esto permite una configuración flexible tanto para desarrollo local (con SQLite) como para entornos de contenedores (con PostgreSQL).
*   **`.env` local:** Se creó un archivo `.env` en el directorio raíz de `AcortadorURL` para definir la `DATABASE_URL` localmente, apuntando a un archivo SQLite para desarrollo y pruebas rápidas. Este archivo `.env` es copiado al contenedor durante la fase de construcción de la imagen.

## Orquestación con Docker Compose

Se diseñó una arquitectura de tres servicios orquestados con `docker-compose.yaml`:

*   **`db` (PostgreSQL):** Un contenedor dedicado a la base de datos PostgreSQL.
    *   Utiliza la imagen `postgres:16-alpine`.
    *   Se configuraron variables de entorno para la base de datos (`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`).
    *   Se mapeó un volumen (`db_data`) para asegurar la persistencia de los datos.
*   **`web` (FastAPI):** El contenedor principal que ejecuta la aplicación FastAPI.
    *   Construye su imagen a partir del `Dockerfile` mejorado.
    *   Utiliza el archivo `.env` local para cargar variables de entorno.
    *   La variable de entorno `DATABASE_URL` se sobrescribe para apuntar al servicio `db` (PostgreSQL) dentro de la red de Docker Compose.
    *   Depende del servicio `db` para asegurar que la base de datos esté lista antes de que la aplicación intente conectarse.
*   **`nginx` (Proxy Inverso):** Un contenedor Nginx que actúa como proxy inverso para el servicio `web`.
    *   Utiliza la imagen `nginx:latest`.
    *   Se montó un archivo `nginx.conf` personalizado para configurar el proxy inverso.
    *   Depende del servicio `web`.
    *   Para evitar conflictos de puerto con otros servicios en el host, se configuró para escuchar en el puerto `8080` del host, reenviando las peticiones al puerto `80` del contenedor Nginx.

## Configuración de Nginx

Se creó el archivo `nginx.conf` para configurar Nginx como proxy inverso. Este archivo define un `upstream` llamado `fastapi_app` que apunta al servicio `web` en el puerto `8000` dentro de la red de Docker Compose. El bloque `server` escucha en el puerto `80` (dentro del contenedor Nginx) y redirige todas las solicitudes al `fastapi_app`, añadiendo cabeceras para preservar la información del host, IP real y protocolo.

## Integración Continua y Despliegue Continuo (CI/CD)

### GitHub Actions para CI (`ci.yml`)

Se mantiene un workflow de Integración Continua (`ci.yml`) que se activa en cada `push` o `pull_request` a la rama `main`. Este workflow se encarga de:
*   Realizar un checkout del código.
*   Configurar el entorno Python 3.11.
*   Instalar las dependencias del proyecto.
*   Ejecutar los tests con `pytest`.

### GitHub Actions para CD - Publicación de Imágenes Docker (`cd.yml`)

Se ha implementado un nuevo workflow de Despliegue Continuo (`cd.yml`) que se activa en cada `push` a la rama `main`. Este workflow es responsable de:
*   Realizar un checkout del código.
*   Autenticarse en el **GitHub Container Registry (GHCR)** utilizando el `GITHUB_TOKEN` proporcionado por GitHub Actions.
*   Construir la imagen Docker de la aplicación `acortadorurl-web` utilizando el `Dockerfile` del proyecto.
*   Publicar la imagen construida en `ghcr.io/${{ github.repository_owner }}/acortadorurl-web:latest`, haciendo que la imagen esté disponible para ser utilizada en cualquier entorno. Se utiliza la caché de GitHub Actions para optimizar las construcciones futuras.

## Verificación

Se verificó el correcto funcionamiento del clúster de Docker Compose mediante:
*   La construcción exitosa de las imágenes y el levantamiento de los servicios con `docker compose up --build -d`.
*   La comprobación del estado de los contenedores con `docker compose ps`, confirmando que todos los servicios (`db`, `web`, `nginx`) estaban activos.
*   Una prueba de accesibilidad a la interfaz de Swagger de la aplicación FastAPI a través del proxy Nginx (`http://localhost:8080/docs`), lo que confirmó la comunicación correcta entre los servicios.

## Próximos Pasos

1.  Actualizar el archivo `CC-25-26/proyectos/hito4.md` con el enlace a esta documentación y al repositorio del proyecto.
2.  Considerar la implementación de tests de integración para validar la conectividad y funcionalidad entre los servicios del clúster de Docker Compose de forma automática.