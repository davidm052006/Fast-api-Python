# Student Card API

Mini API REST construida con **FastAPI** para consultar y registrar estudiantes.

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual (Windows)
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar la API

```bash
uvicorn main:app --reload
```

La API estará disponible en: http://127.0.0.1:8000

Documentación interactiva (Swagger): http://127.0.0.1:8000/docs

---

## Endpoints

### GET /students/{id}
Consulta un estudiante por su ID.

**Ejemplo:**
```
GET http://127.0.0.1:8000/students/1
```

**Respuesta exitosa (200):**
```json
{
  "id": 1,
  "name": "Laura Gómez",
  "email": "laura.gomez@email.com",
  "program": "Análisis y Desarrollo de Software",
  "active": true
}
```

**Estudiante no encontrado (404):**
```json
{
  "detail": "Student not found"
}
```

---

### POST /students
Registra un nuevo estudiante.

**Ejemplo:**
```
POST http://127.0.0.1:8000/students
Content-Type: application/json
```

**Cuerpo:**
```json
{
  "name": "Carlos Pérez",
  "email": "carlos.perez@email.com",
  "program": "Gestión de Redes de Datos",
  "active": true
}
```

**Respuesta exitosa (201):**
```json
{
  "id": 3,
  "name": "Carlos Pérez",
  "email": "carlos.perez@email.com",
  "program": "Gestión de Redes de Datos",
  "active": true
}
```

---

### GET /students?active=true
Lista estudiantes filtrados por estado.

**Ejemplos:**
```
GET http://127.0.0.1:8000/students?active=true
GET http://127.0.0.1:8000/students?active=false
GET http://127.0.0.1:8000/students        ← devuelve todos
```

**Respuesta (200):**
```json
[
  {
    "id": 1,
    "name": "Laura Gómez",
    "email": "laura.gomez@email.com",
    "program": "Análisis y Desarrollo de Software",
    "active": true
  }
]
```

---

## Códigos HTTP utilizados

| Código | Significado              |
|--------|--------------------------|
| 200    | OK                       |
| 201    | Created                  |
| 404    | Not Found                |
| 422    | Unprocessable Entity     |
