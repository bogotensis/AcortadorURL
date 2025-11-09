# Proyecto de Prácticas de Cloud Computing: Acortador de URLs con Analíticas

Este repositorio contiene el proyecto de prácticas para la asignatura de Cloud Computing: Fundamentos e Infraestructuras. El proyecto consiste en el desarrollo de un **Acortador de URLs con Analíticas**, una aplicación que permite a los usuarios generar versiones cortas de URLs largas y, además, proporciona estadísticas detalladas sobre el uso de estas URLs acortadas.

## Descripción del Proyecto

El objetivo principal de este proyecto es implementar un servicio robusto y escalable que cumpla con los siguientes requisitos:

*   **Acortamiento de URLs:** Permitir a los usuarios enviar una URL larga y recibir a cambio una URL corta y única.
*   **Redirección:** Cuando un usuario accede a una URL corta, el servicio debe redirigirlo automáticamente a la URL larga original.
*   **Analíticas de Uso:** Registrar y proporcionar datos estadísticos sobre cada acceso a las URLs acortadas, incluyendo información como la fecha y hora del acceso, el agente de usuario (navegador/dispositivo), y posiblemente la ubicación geográfica (sin almacenar datos personales identificables).

### Justificación y Cumplimiento de Requisitos de la Asignatura

Este proyecto ha sido diseñado para cumplir con los requisitos de los hitos de la asignatura de la siguiente manera:

*   **Lógica de Negocio Aceptable (Hito 1):** Va más allá de un simple almacenamiento de datos. La generación de códigos únicos, la gestión de redirecciones y, especialmente, la recolección y procesamiento de datos de analíticas, constituyen una lógica de negocio compleja y relevante.
*   **Arquitectura Basada en Servidor y Beneficios de la Nube (Hito 1):** Es inherentemente una aplicación basada en servidor que maneja peticiones HTTP. Se beneficia enormemente de un despliegue en la nube por su necesidad de escalabilidad (para manejar un alto volumen de clics), procesamiento de datos (para las analíticas) y alta disponibilidad.
*   **Diseño de Microservicios (Hito 3):** El proyecto se presta a una arquitectura de microservicios, donde la funcionalidad de acortamiento de URLs y la de analíticas pueden ser servicios separados que interactúan entre sí. Esto permitirá explorar la separación de la lógica de negocio de la lógica de la API, la creación de APIs REST consistentes y la integración de sistemas de logging.
*   **Integración Continua (Hito 2):** La naturaleza modular del proyecto facilita la implementación de pruebas unitarias y de integración exhaustivas. Se configurará un sistema de Integración Continua (CI) para automatizar la ejecución de estas pruebas en cada cambio de código, asegurando la calidad y estabilidad del proyecto.

## Stack Tecnológico Propuesto

Para la implementación de este proyecto, se utilizará el siguiente stack tecnológico:

*   **Lenguaje de Programación:** Python
*   **Framework Web (Microservicios):** FastAPI
*   **Framework de Pruebas:** Pytest
*   **Gestor de Tareas:** Makefile
*   **Sistema de Integración Continua (CI):** GitHub Actions
