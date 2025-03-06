# Playground Final Project

## Descripción
Este proyecto es una aplicación web estilo blog donde los usuarios pueden registrarse, iniciar sesión, gestionar su perfil, enviar mensajes y crear, editar y eliminar publicaciones. Además, incluye una sección "Acerca de mí" y un panel de administración.

## Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MarianoBustamante/entrega_final.git
   cd playground
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
5. Crear un superusuario para acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```
6. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

## Orden para probar la aplicación

### 1. Página de inicio
Acceder a `http://127.0.0.1:8000/` para ver la página principal con las opciones de navegación.

### 2. Registro e inicio de sesión
- Ir a `http://127.0.0.1:8000/cuentas/registro/` para crear un usuario.
- Iniciar sesión en `http://127.0.0.1:8000/cuentas/login/`.

### 3. Gestión de perfil
- Acceder al perfil en `http://127.0.0.1:8000/cuentas/perfil/`.
- Editar perfil y cambiar contraseña desde esa vista.

### 4. Funcionalidad de "Acerca de mí"
- En la barra de navegación, hacer clic en "Acerca de mí" o acceder a `http://127.0.0.1:8000/about/`.

### 5. Creación y gestión de publicaciones
- Ir a `http://127.0.0.1:8000/pages/` para ver la lista de publicaciones.
- Si no hay publicaciones, debe aparecer el mensaje "No hay páginas aún".
- Crear una nueva publicación en `http://127.0.0.1:8000/pages/crear/`.
- Desde la lista, acceder al detalle de una publicación.
- Editar o eliminar publicaciones (solo si estás logueado).

### 6. Mensajería entre usuarios
- Ir a `http://127.0.0.1:8000/mensajes/` para ver la bandeja de entrada.
- Enviar un mensaje a otro usuario desde `http://127.0.0.1:8000/mensajes/enviar/`.

### 7. Cierre de sesión
- Desde la barra de navegación, hacer clic en "Cerrar sesión".

## Consideraciones Finales
- La aplicación utiliza herencia de templates para mantener un diseño uniforme.
- Se han implementado CBVs y mixins para optimizar el código.
- El proyecto no incluye la base de datos (`db.sqlite3`) en el repositorio.
- Se recomienda probar todo antes de subir cambios a GitHub.

## Video de Presentación
El video que muestra el funcionamiento del proyecto se encuentra en https://drive.google.com/file/d/1iOufqNWDJDav6mk1PXnzZs5_9cxUZrq9/view?usp=sharing

