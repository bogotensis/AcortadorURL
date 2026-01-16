# Hito 5: Despliegue de la aplicación en Render

## Introducción

Este hito se centró en el despliegue de la aplicación "Acortador de URLs" en un entorno de Plataforma como Servicio (PaaS) y la integración de herramientas de observabilidad, así como la realización de pruebas de rendimiento.

## Elección del IaaS/PaaS

Para el despliegue de la aplicación se eligió **Render** (https://render.com/) como Plataforma como Servicio (PaaS) por las siguientes razones:

*   **Soporte nativo de Docker:** La aplicación está contenerizada con Docker, y Render permite desplegar directamente desde un `Dockerfile`.
*   **Integración con GitHub:** Facilita el despliegue continuo (CD) al conectarse directamente con el repositorio de GitHub y activar despliegues automáticos en cada `push` a la rama `main`.
*   **Capa Gratuita:** Ofrece una capa gratuita para servicios web y bases de datos PostgreSQL, adecuada para proyectos de desarrollo y académicos.
*   **Regiones Europeas:** Permite el despliegue en centros de datos ubicados en Europa, cumpliendo con los requisitos de la asignatura.
*   **Configuración Declarativa:** Aunque se puede configurar a través de la interfaz web, Render también soporta la definición de la infraestructura mediante archivos `render.yaml`, lo cual cumple con el requisito de "configuración debe definirse en un fichero".

## Configuración del Despliegue en Render

El despliegue en Render se realizó configurando dos servicios:

### 1. Base de Datos PostgreSQL

Se creó un servicio de base de datos PostgreSQL gestionado en Render (`acortadorurl-db`) con las siguientes características:

*   **Nombre:** `acortadorurl-db`
*   **Región:** Frankfurt (eu-central-1)
*   **Base de Datos:** `shortener_db`
*   **Usuario:** `user`
*   Render generó una `Internal Database URL` que se utilizó para conectar la aplicación web.

### 2. Servicio Web (Aplicación FastAPI)

Se creó un servicio web en Render (`acortadorurl-web`) conectado al repositorio de GitHub `bogotensis/AcortadorURL` con las siguientes configuraciones clave:

*   **Nombre:** `acortadorurl-web`
*   **Región:** Frankfurt (eu-central-1) (misma que la base de datos)
*   **Branch:** `main`
*   **Root Directory:** `.`
*   **Runtime:** Docker (detectado automáticamente por la presencia del `Dockerfile`)
*   **Build Command:** (vacío, Render utiliza el `Dockerfile`)
*   **Start Command:** `/home/app/.local/bin/uvicorn acortadorurl.main:app --host 0.0.0.0 --port 8000`
*   **Variables de Entorno:**
    *   `DATABASE_URL`: Se configuró con la `Internal Database URL` obtenida de la base de datos PostgreSQL de Render. Esto sobrescribe la configuración local del `.env` y conecta la aplicación a la base de datos remota.

Render automáticamente gestiona el proceso de construcción de la imagen Docker utilizando el `Dockerfile` del repositorio y despliega el servicio. El despliegue se activa automáticamente con cada `push` a la rama `main`.

**URL de la aplicación desplegada:** `https://acortadorurl-z2xj.onrender.com`

## Observabilidad

Para cumplir con los requisitos de observabilidad, se implementaron las siguientes estrategias:

*   **Logs en Tiempo Real:** Render proporciona un sistema de logs integrado para cada servicio. La aplicación FastAPI ya utiliza el módulo `logging` de Python (`logging.basicConfig(level=logging.INFO)` y `logger = logging.getLogger(__name__)`) para emitir mensajes informativos sobre el estado de la aplicación, solicitudes entrantes, creación de URLs y redirecciones. Estos logs son accesibles desde el dashboard de Render y son fundamentales para monitorear el comportamiento de la aplicación y diagnosticar problemas.

*   **Pruebas de Rendimiento:** Las pruebas de rendimiento actúan como una forma de obtener métricas de desempeño cuantitativas. Los resultados de estas pruebas proporcionan información sobre la capacidad de respuesta y la estabilidad de la aplicación bajo carga.

## Pruebas de Rendimiento

Se realizó una prueba de carga en la aplicación desplegada utilizando `ApacheBench` (`ab`) para simular tráfico y evaluar su rendimiento.

**Metodología:**
1.  Se creó una URL corta de prueba mediante una petición `POST` al endpoint `/shorten` de la aplicación desplegada.
    *   `curl -X POST -H "Content-Type: application/json" -d '{"original_url": "https://www.google.com"}' https://acortadorurl-z2xj.onrender.com/shorten`
    *   **URL corta generada:** `https://acortadorurl-z2xj.onrender.com/KVcGTG`
2.  Se ejecutó `ApacheBench` con 1000 solicitudes y 50 peticiones concurrentes a la URL corta generada.
    *   `ab -n 1000 -c 50 https://acortadorurl-z2xj.onrender.com/KVcGTG`

**Resultados:**

```
Server Software:        uvicorn
Server Hostname:        acortadorurl-z2xj.onrender.com
Server Port:            443
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,256,256
TLS Server Name:        acortadorurl-z2xj.onrender.com

Document Path:          /KVcGTG
Document Length:        0 bytes

Concurrency Level:      50
Time taken for tests:   19.943 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      312000 bytes
HTML transferred:       0 bytes
Requests per second:    50.14 [#/sec] (mean)
Time per request:       997.139 [ms] (mean)
Time per request:       19.943 [ms] (mean, across all concurrent requests)
Transfer rate:          15.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       22   35  12.6     32     116
Processing:   173  935 185.2    937    1844
Waiting:      165  934 185.2    937    1844
Total:        203  970 189.0    986    1874

Percentage of the requests served within a certain time (ms)
  50%    986
  66%   1004
  75%   1095
  80%   1100
  90%   1197
  95%   1298
  98%   1439
  99%   1595
 100%   1874 (longest request)
```

**Análisis de Resultados:**

*   La aplicación manejó las 1000 solicitudes sin fallos.
*   Se observó un promedio de 50.14 solicitudes por segundo.
*   El tiempo promedio por solicitud fue de aproximadamente 997 ms (casi 1 segundo), con un máximo de 1.8 segundos.

Estos resultados son satisfactorios para un despliegue inicial en una capa gratuita, demostrando que la aplicación es funcional y capaz de gestionar una carga moderada. Para un entorno de producción, se buscarían tiempos de respuesta más bajos y se realizarían optimizaciones adicionales.

## Próximos Pasos

1.  Actualizar `CC-25-26/proyectos/hito5.md` con el enlace a esta documentación y al repositorio del proyecto.