# Acortador de URLs con Analíticas

[![CI](https://github.com/bogotensis/AcortadorURL/actions/workflows/ci.yml/badge.svg)](https://github.com/bogotensis/AcortadorURL/actions/workflows/ci.yml)

Este proyecto es un servicio para acortar URLs, desarrollado como parte de la asignatura de Cloud Computing. La aplicación está construida con un stack moderno que incluye Python y FastAPI, y se encuentra totalmente contenerizada con Docker para un despliegue reproducible y escalable.

---

## 🚀 Aplicación en Producción

La aplicación está desplegada en Render y puedes interactuar con ella aquí:

*   **URL Base:** [https://acortadorurl-z2xj.onrender.com](https://acortadorurl-z2xj.onrender.com)
*   **Documentación de la API (Swagger):** [https://acortadorurl-z2xj.onrender.com/docs](https://acortadorurl-z2xj.onrender.com/docs)

---

## ✨ Características

*   **Acortamiento de URLs:** Genera una URL corta y única a partir de una URL larga.
*   **Redirección:** Redirige de forma transparente de la URL corta a la original.
*   **API RESTful:** Interfaz limpia y documentada para interactuar con el servicio.
*   **Contenerizado:** Despliegue reproducible y aislado con Docker.

---

## 🛠️ Stack Tecnológico

*   **Backend:** Python, FastAPI
*   **Base de Datos:** PostgreSQL (en producción/Docker) y SQLite (para desarrollo local)
*   **Contenerización:** Docker, Docker Compose
*   **Proxy Inverso:** Nginx
*   **CI/CD:** GitHub Actions
*   **Despliegue (PaaS):** Render
*   **Testing:** Pytest
*   **Gestor de Tareas:** Makefile

---

## 🏁 Cómo Empezar (Desarrollo)

### Prerrequisitos
*   Docker y Docker Compose
*   Opcional (para entorno local): Python 3.11+

### Opción 1: Ejecutar con Docker Compose (Recomendado)

1.  **Clona el repositorio.**
2.  **Levanta los servicios:**
    ```bash
    docker compose up -d --build
    ```
La aplicación estará disponible en `http://localhost:8080`.

### Opción 2: Ejecutar en Entorno Local con Python

1.  **Instala las dependencias:**
    ```bash
    make install
    ```
2.  **Inicia el servidor:**
    ```bash
    make run
    ```
La aplicación estará disponible en `http://127.0.0.1:8000`.

---

## 🧪 Pruebas

Para ejecutar la suite de tests, usa el siguiente comando:
```bash
make test
```

---

## 📚 Cumplimiento de Hitos del Proyecto

Este proyecto se ha desarrollado siguiendo una serie de hitos definidos por la asignatura de Cloud Computing. A continuación se resume el cumplimiento de cada uno y se enlaza a la documentación detallada.

### Hito 1: Repositorio y Definición del Proyecto
Se configuró el repositorio inicial del proyecto, adoptando buenas prácticas como el uso de `.gitignore`, licencia, commits atómicos y la estructura del proyecto. Se definió el alcance del "Acortador de URLs" y el stack tecnológico inicial.
*   **[Ver documentación completa del Hito 1](docs/hito1.md)**

### Hito 2: Integración Continua (CI)
Se implementó un pipeline de Integración Continua con GitHub Actions. Se configuró un `Makefile` para automatizar tareas (instalación y testing) y se utilizó `pytest` para las pruebas, asegurando que cada cambio en el código sea verificado automáticamente.
*   **[Ver documentación completa del Hito 2](docs/hito2.md)**

### Hito 3: Diseño de Microservicios
Se diseñó y desarrolló el primer microservicio usando FastAPI. Se aplicó una arquitectura por capas para separar la lógica de negocio de la API REST, se implementaron las rutas para acortar y redirigir URLs y se integró un sistema de `logging` para la observabilidad.
*   **[Ver documentación completa del Hito 3](docs/hito3.md)**

### Hito 4: Contenedores y Orquestación
Se contenerizó la aplicación con Docker y se orquestó un clúster de tres servicios (FastAPI, PostgreSQL, Nginx) usando Docker Compose. Se configuró un pipeline de Despliegue Continuo (CD) para publicar la imagen de la aplicación en GitHub Packages.
*   **[Ver documentación completa del Hito 4](docs/hito4.md)**

### Hito 5: Despliegue en PaaS
La aplicación se desplegó exitosamente en la plataforma **Render**. Se configuraron los servicios de base de datos (PostgreSQL) y web (Docker), se verificó la observabilidad a través de los logs y se realizaron pruebas de rendimiento con ApacheBench para validar el despliegue.
*   **[Ver documentación completa del Hito 5](docs/hito5.md)**

---
## 📄 Licencia
Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.
