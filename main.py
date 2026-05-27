from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr, field_validator

app = FastAPI(
    title="Student Card API",
    description="API para consultar y registrar estudiantes",
    version="1.0"
)

# Base de datos en memoria
students = [
    {
        "id": 1,
        "name": "Laura Gómez",
        "email": "laura.gomez@email.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    {
        "id": 2,
        "name": "Andrés Martínez",
        "email": "andres.martinez@email.com",
        "program": "Producción Multimedia",
        "active": False
    },
    {
        "id": 3,
        "name": "Carlos Pérez",
        "email": "carlos.perez@email.com",
        "program": "Gestión de Redes de Datos",
        "active": True
    },
    {
        "id": 4,
        "name": "Valentina Torres",
        "email": "valentina.torres@email.com",
        "program": "Análisis y Desarrollo de Software",
        "active": False
    },
    {
        "id": 5,
        "name": "Miguel Ángel Ruiz",
        "email": "miguel.ruiz@email.com",
        "program": "Técnico en Sistemas",
        "active": True
    }
]


# Modelo de entrada para crear un estudiante
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    program: str
    active: bool

    @field_validator("name", "program")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Este campo no puede estar vacío")
        return v


# GET /students/{id} — consultar un estudiante por ID
@app.get("/students/{id}", status_code=200)
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


# POST /students — registrar un nuevo estudiante
@app.post("/students", status_code=201)
def create_student(student_data: StudentCreate):
    new_id = students[-1]["id"] + 1 if students else 1

    new_student = student_data.dict()
    new_student["id"] = new_id

    students.append(new_student)
    return new_student


# GET /students?active=true|false — listar estudiantes por estado
@app.get("/students", status_code=200)
def get_students(active: bool = Query(None)):
    if active is None:
        return students

    filtered = [s for s in students if s["active"] == active]
    return filtered
