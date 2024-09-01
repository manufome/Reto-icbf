# Sistema de Gestión ICBF

## Descripción

Este proyecto es un sistema de gestión para el Instituto Colombiano de Bienestar Familiar (ICBF). Está diseñado para administrar información relacionada con jardines infantiles, niños, madres comunitarias y acudientes.

## Características principales

-   Gestión de usuarios (administradores, madres comunitarias, acudientes)
-   Administración de jardines infantiles
-   Registro y seguimiento de niños
-   Control de asistencia
-   Generación de reportes
-   Sistema de publicaciones

## Tecnologías utilizadas

-   Django (Backend)
-   HTML, CSS, JavaScript (Frontend)
-   Tailwind CSS (Estilos)
-   SQLite (Base de datos)
-   Django Background Tasks (Tareas programadas)

## Instalación

1. Clona el repositorio
2. Crea un entorno virtual:
    ```
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```
5. Configura la base de datos en `settings.py`
6. Ejecuta las migraciones:
    ```
    python manage.py migrate
    ```
7. Crea un superusuario:
    ```
    python manage.py createsuperuser
    ```
8. Inicia el servidor de desarrollo:
    ```
    python manage.py runserver
    ```

## Estructura del proyecto

-   `project_icbf/`: Directorio principal del proyecto
    -   `usuarios/`: Aplicación para gestión de usuarios
    -   `jardines/`: Aplicación para gestión de jardines
    -   `niños/`: Aplicación para gestión de niños
    -   `publicaciones/`: Aplicación para gestión de publicaciones
    -   `reportes/`: Aplicación para generación de reportes
    -   `templates/`: Plantillas HTML
    -   `static/`: Archivos estáticos (CSS, JS, imágenes)
    -   `media/`: Archivos subidos por los usuarios

## Comandos útiles

-   Poblar la base de datos con datos de prueba:
    ```
    python manage.py populate
    ```
-   Crear tareas programadas:
    ```
    python manage.py schedule_tasks
    ```
-   Correr tareas programadas:
    ```
    python manage.py process_tasks
    ```
