# Student Card API

API REST para la gestión de estudiantes construida con FastAPI. Este proyecto demuestra mejores prácticas en desarrollo de APIs modernas con Python.

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Documentación de Endpoints](#documentación-de-endpoints)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Modelos de Datos](#modelos-de-datos)
- [Tecnologías](#tecnologías)

---

## Características

- **CRUD Completo**: Crear, leer, actualizar y eliminar estudiantes
- **Validación de Datos**: Con Pydantic para garantizar integridad de datos
- **Health Checks**: Endpoints para monitoreo de disponibilidad del servidor
- **Echo Service**: Endpoint para pruebas de conectividad
- **Documentación Automática**: Swagger UI y ReDoc integrados
- **Rutas Organizadas**: Código modular con routers separados
- **Manejo de Errores**: Respuestas HTTP apropiadas con mensajes descriptivos
- **Filtrado Avanzado**: Posibilidad de filtrar estudiantes por estado activo

---

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a la terminal o línea de comandos

---

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd api-estudiantes
```

### Paso 2: Crear un entorno virtual

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Uso

### Iniciar el servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: **http://127.0.0.1:8000**

### Acceder a la documentación interactiva

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

El flag `--reload` reinicia el servidor automáticamente cuando detecta cambios en los archivos (muy útil en desarrollo).

---

## Estructura del Proyecto

```
api-estudiantes/
├── main.py                          # Punto de entrada de la aplicación
├── requirements.txt                 # Dependencias del proyecto
├── .gitignore                       # Archivos a ignorar en Git
├── README.md                        # Este archivo
└── APP/
    ├── __init__.py                  # Inicializador del paquete
    ├── main.py                      # Lógica principal de FastAPI
    └── routers/
        ├── __init__.py              # Inicializador del paquete routers
        ├── echo.py                  # Router para servicio de echo
        └── health.py                # Router para health checks
```

---

## Documentación de Endpoints

### Endpoints de Estudiantes

#### GET `/students` - Listar estudiantes

Obtiene la lista de todos los estudiantes. Puedes filtrar por estado si lo necesitas.

**Parámetros de Query:**
- `active` (boolean, opcional): Filtrar por estado activo. Valores: `true`, `false`

**Ejemplo:**
```bash
curl "http://127.0.0.1:8000/students"
curl "http://127.0.0.1:8000/students?active=true"
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "David Mateo",
    "email": "david.mateo@gmail.com",
    "program": "Análisis y Desarrollo de Software",
    "active": true
  }
]
```

---

#### GET `/students/{student_id}` - Obtener un estudiante

Trae los detalles de un estudiante específico por su ID.

**Parámetros:**
- `student_id` (integer): ID del estudiante

**Ejemplo:**
```bash
curl "http://127.0.0.1:8000/students/1"
```

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "name": "David Mateo",
  "email": "david.mateo@gmail.com",
  "program": "Análisis y Desarrollo de Software",
  "active": true
}
```

**Cuando no existe (404):**
```json
{
  "detail": "Student not found"
}
```

---

#### POST `/students` - Crear un estudiante

Agrega un nuevo estudiante al sistema.

**Body (JSON):**
```json
{
  "name": "Juan Pérez",
  "email": "juan.perez@example.com",
  "program": "Análisis y Desarrollo de Software",
  "active": true
}
```

**Ejemplo:**
```bash
curl -X POST "http://127.0.0.1:8000/students" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan.perez@example.com",
    "program": "Análisis y Desarrollo de Software",
    "active": true
  }'
```

**Respuesta (201 Created):**
```json
{
  "id": 3,
  "name": "Juan Pérez",
  "email": "juan.perez@example.com",
  "program": "Análisis y Desarrollo de Software",
  "active": true
}
```

---

#### PUT `/students/{student_id}` - Actualizar un estudiante

Modifica los datos de un estudiante existente.

**Parámetros:**
- `student_id` (integer): ID del estudiante a modificar

**Body (JSON):**
```json
{
  "name": "Juan Carlos Pérez",
  "email": "juancarlos@example.com",
  "program": "Producción Multimedia",
  "active": false
}
```

**Ejemplo:**
```bash
curl -X PUT "http://127.0.0.1:8000/students/3" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Carlos Pérez",
    "email": "juancarlos@example.com",
    "program": "Producción Multimedia",
    "active": false
  }'
```

**Respuesta (200 OK):**
```json
{
  "id": 3,
  "name": "Juan Carlos Pérez",
  "email": "juancarlos@example.com",
  "program": "Producción Multimedia",
  "active": false
}
```

---

#### DELETE `/students/{student_id}` - Eliminar un estudiante

Borra un estudiante del sistema.

**Parámetros:**
- `student_id` (integer): ID del estudiante a eliminar

**Ejemplo:**
```bash
curl -X DELETE "http://127.0.0.1:8000/students/3"
```

**Respuesta (200 OK):**
```json
{
  "message": "Student eliminado"
}
```

---

### Endpoints de Health Check

#### GET `/health/live` - Verificar disponibilidad

Comprueba si el servidor está activo.

**Respuesta:**
```json
{
  "status": "alive"
}
```

---

#### GET `/health/ready` - Verificar preparación

Comprueba si el servidor está listo para recibir solicitudes.

**Respuesta:**
```json
{
  "status": "ready"
}
```

---

### Endpoint de Echo

#### POST `/echo` - Echo de mensaje

Devuelve el mensaje que recibe. Útil para hacer pruebas rápidas.

**Body (JSON):**
```json
{
  "message": "Hola API"
}
```

**Ejemplo:**
```bash
curl -X POST "http://127.0.0.1:8000/echo" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola API"}'
```

**Respuesta:**
```json
{
  "message": "Hola API"
}
```

---

## Ejemplos de Uso

### Flujo completo

```bash
# Crear un nuevo estudiante
curl -X POST "http://127.0.0.1:8000/students" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Carlos López",
    "email": "carlos.lopez@example.com",
    "program": "Análisis y Desarrollo de Software",
    "active": true
  }'

# Listar todos los estudiantes
curl "http://127.0.0.1:8000/students"

# Obtener un estudiante específico
curl "http://127.0.0.1:8000/students/4"

# Actualizar estudiante
curl -X PUT "http://127.0.0.1:8000/students/4" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Carlos María López",
    "email": "carlosm.lopez@example.com",
    "program": "Análisis y Desarrollo de Software",
    "active": true
  }'

# Filtrar estudiantes activos
curl "http://127.0.0.1:8000/students?active=true"

# Eliminar estudiante
curl -X DELETE "http://127.0.0.1:8000/students/4"
```

---

## Modelos de Datos

### StudentCreate

Modelo para crear o actualizar un estudiante:

```python
class StudentCreate(BaseModel):
    name: str              # Nombre completo (mínimo 1 carácter)
    email: str             # Correo electrónico
    program: str           # Programa de formación (mínimo 1 carácter)
    active: bool           # Estado del estudiante (true/false)
```

### Student

Modelo completo de estudiante (hereda de StudentCreate):

```python
class Student(StudentCreate):
    id: int                # Identificador único (asignado automáticamente)
```

---

## Tecnologías

| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| FastAPI | 0.136.3 | Framework web moderno y rápido |
| Uvicorn | 0.48.0 | Servidor ASGI de alto rendimiento |
| Pydantic | 2.13.4 | Validación de datos y serialización |
| Python | 3.13+ | Lenguaje de programación |

---

## Características Técnicas

### Validación de Datos

Todos los campos son validados automáticamente por Pydantic:
- Los campos `name` y `program` requieren al menos 1 carácter
- El campo `email` debe tener formato válido
- El campo `active` debe ser booleano (true/false)

### Códigos de Estado HTTP

- **200 OK**: Solicitud exitosa
- **201 Created**: Recurso creado exitosamente
- **404 Not Found**: Recurso no encontrado
- **422 Unprocessable Entity**: Datos inválidos

### Almacenamiento

Los datos se almacenan en memoria durante la ejecución del servidor. Esto significa que si reinicias la aplicación, todos los cambios se pierden.

Si necesitas persistencia, considera integrar una base de datos como PostgreSQL, MongoDB o SQLite.

---

## Notas Importantes

1. **Datos en Memoria**: Los datos se pierden al reiniciar el servidor
2. **Entorno Virtual**: Usa siempre un entorno virtual para aislar las dependencias
3. **Desarrollo vs Producción**: El flag `--reload` es para desarrollo, no uses en producción

---

## Autor

Proyecto educativo - SENA, Trimestre 4
