# Hito 1: Repositorio de Prácticas y Definición del Proyecto

Este documento detalla el cumplimiento de los requisitos establecidos en el Hito 1 de la asignatura de Cloud Computing.

## 1. Definición del Proyecto

La descripción del proyecto, su justificación y el stack tecnológico se encuentran en el fichero principal del repositorio:
- [README.md](../README.md)

El proyecto "Acortador de URLs con Analíticas" cumple con los requisitos de tener una lógica de negocio aceptable, estar basado en servidor y beneficiarse de un despliegue en la nube.

## 2. Configuración del Entorno y Buenas Prácticas

A continuación, se confirma la configuración del entorno de desarrollo y la adopción de las buenas prácticas solicitadas.

### Configuración del Entorno

- **[X] Descarga de `git`:** Se utiliza `git` desde la línea de órdenes para gestionar el control de versiones.
- **[X] Creación de par de claves SSH:** Se ha generado un par de claves SSH (`id_ed25519`) y la clave pública ha sido añadida a la configuración de la cuenta de GitHub, permitiendo la autenticación segura con el repositorio.
- **[X] Configuración de `git`:** El nombre de usuario y el correo electrónico han sido configurados globalmente en `git` para la correcta autoría de los *commits*.
- **[X] Perfil de GitHub:** El perfil de GitHub del usuario ha sido actualizado para incluir una imagen de perfil, nombre completo, ciudad y universidad.
- **[X] Segundo Factor de Autenticación (2FA):** Se ha activado el 2FA en la cuenta de GitHub para incrementar la seguridad.

### Adopción de Buenas Prácticas

- **[X] Fichero `.gitignore`:** Se ha creado y configurado un fichero `.gitignore` desde el inicio del proyecto para excluir ficheros generados, compilados o de configuración local.
- **[X] Licencia:** El repositorio incluye un fichero `LICENSE` con la licencia del proyecto.
- **[X] Commits Atómicos y Descriptivos:** Se sigue la práctica de realizar *commits* atómicos que abarcan una única funcionalidad y de escribir mensajes descriptivos que explican el propósito del cambio.
- **[X] Uso de Issues y Milestones:** Se utilizará el sistema de *Issues* y *Milestones* de GitHub para la gestión de tareas y la planificación de los hitos del proyecto. Los *commits* harán referencia a los *issues* correspondientes para mantener la trazabilidad.
- **[X] No inclusión de código ajeno:** No se incluirá código que no sea propio directamente en el repositorio. Las dependencias se gestionarán a través de ficheros de requisitos.
- **[X] No inclusión de binarios:** No se publicarán ficheros binarios en el repositorio. Se utilizarán los *releases* de GitHub para este propósito si fuera necesario.
- **[_] Sincronización con Repositorio del Profesor:** Se adoptará la práctica de sincronizar el *fork* del repositorio de la asignatura (`git pull --rebase`) antes de realizar un *pull request* para evitar conflictos y *merge commits*.

## 3. Entrega del Hito

Para la entrega de este hito, se ha realizado un *fork* del repositorio del profesor y se ha creado un *Pull Request* con el enlace a este documento en el fichero `proyectos/hito1.md`.
