# Hito 2: Integración Continua

Este documento detalla la implementación de la Integración Continua (CI) para el proyecto "Acortador de URLs con Analíticas", siguiendo los requisitos del Hito 2 de la asignatura de Cloud Computing.

## 1. Elección y Configuración de Herramientas

Para la implementación de la CI, se han seleccionado las siguientes herramientas, justificando su elección:

### Gestor de Tareas: `Makefile`

-   **Elección:** Se ha optado por `Makefile` como gestor de tareas.
-   **Justificación:** `Makefile` es una herramienta estándar y ampliamente utilizada en proyectos de software para automatizar tareas repetitivas como la instalación de dependencias, la ejecución de tests, la construcción de proyectos, etc. Su simplicidad y su capacidad para definir objetivos (`targets`) y sus dependencias lo hacen ideal para este proyecto. Permite que tanto en entornos locales como en el CI, las tareas se lancen de forma consistente.
-   **Configuración:** Se ha creado un `Makefile` en la raíz del proyecto con los siguientes objetivos:
    -   `install`: Instala las dependencias de Python listadas en `requirements.txt`.
    -   `test`: Ejecuta los tests del proyecto utilizando `pytest`.

### Biblioteca de Aserciones y Marco de Pruebas: `Pytest`

-   **Elección:** Se ha seleccionado `Pytest` como marco de pruebas y su sistema de aserciones integrado.
-   **Justificación:** `Pytest` es un *framework* de pruebas maduro y muy popular en el ecosistema Python. Ofrece una sintaxis de pruebas simple y legible, autodescubrimiento de tests, una gran cantidad de plugins y una excelente capacidad para generar informes detallados. Su sistema de aserciones (`assert`) es potente y no requiere una biblioteca externa adicional, lo que simplifica el código de las pruebas. Se alinea con un enfoque de desarrollo basado en pruebas (TDD) por su facilidad de uso y flexibilidad.
-   **Configuración:** Se ha creado un directorio `tests/` con un archivo `test_main.py` que contiene una prueba inicial para la lógica de negocio.

### Sistema de Integración Continua (CI): `GitHub Actions`

-   **Elección:** Se ha elegido `GitHub Actions` como sistema de CI.
-   **Justificación:** `GitHub Actions` es una solución de CI/CD integrada directamente en GitHub, lo que facilita su configuración y gestión al estar en el mismo entorno que el repositorio de código. Es gratuito para proyectos públicos y ofrece una gran flexibilidad para definir flujos de trabajo personalizados. Su integración nativa con el repositorio permite que los flujos de trabajo se activen automáticamente en eventos como `push` o `pull_request`.
-   **Configuración:** Se ha creado un archivo de flujo de trabajo (`.github/workflows/ci.yml`) que:
    -   Se activa en cada `push` y `pull_request` a la rama `main`.
    -   Configura un entorno de Python 3.9.
    -   Instala las dependencias del proyecto usando `make install`.
    -   Ejecuta los tests del proyecto usando `make test`.

## 2. Implementación y Ejecución de Tests

Se ha implementado una función de ejemplo (`mi_primera_funcion`) en `acortadorurl/main.py` y una prueba correspondiente en `tests/test_main.py` para demostrar la configuración de los tests.

La ejecución de los tests se realiza localmente mediante el comando `make test`, y automáticamente en el CI a través de `GitHub Actions` tras cada `push` o `pull_request`.

## 3. Entrega del Hito

Para la entrega de este hito, se ha actualizado el repositorio con los ficheros de configuración de CI, el código inicial y los tests, y se ha realizado un `push` a la rama `main`. Este documento (`docs/hito2.md`) ha sido creado para justificar las decisiones técnicas tomadas.
