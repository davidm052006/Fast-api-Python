from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

from .routers.echo import router as echo_router
from .routers.health import router as health_router

app = FastAPI(
    title="Student Card API",
    description="API para gestionar estudiantes y servicios de health/echo.",
    version="1.1.0"
)

# Datos en memoria
students_db = [
    {
        "id": 1,
        "name": "David Mateo",
        "email": "david.mateo@gmail.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    {
        "id": 2,
        "name": "Andrés Martínez",
        "email": "andres.martinez@gmail.com",
        "program": "Producción Multimedia",
        "active": False
    }
]

# Contador para IDs
next_id = 3


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, title="Nombre completo")
    email: str = Field(..., title="Correo electrónico")
    program: str = Field(..., min_length=1, title="Programa de formación")
    active: bool = Field(..., title="Estado del estudiante")


class Student(StudentCreate):
    id: int = Field(..., title="Identificador único")


app.include_router(echo_router)
app.include_router(health_router)


@app.get("/")
def root() -> dict:
    return {"message": "Bienvenido a Student Card API"}


@app.get("/students", response_model=List[Student], status_code=status.HTTP_200_OK)
def list_students(active: Optional[bool] = Query(None, title="Filtrar por estado")) -> List[Student]:
    if active is None:
        return students_db
    return [student for student in students_db if student["active"] == active]


@app.get("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student(student_id: int) -> Student:
    for student in students_db:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate) -> Student:
    global next_id
    new_student = {
        "id": next_id,
        "name": student.name,
        "email": student.email,
        "program": student.program,
        "active": student.active
    }
    students_db.append(new_student)
    next_id += 1
    return new_student


@app.put("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student: StudentCreate) -> Student:
    for index, existing_student in enumerate(students_db):
        if existing_student["id"] == student_id:
            updated_student = {
                "id": student_id,
                "name": student.name,
                "email": student.email,
                "program": student.program,
                "active": student.active
            }
            students_db[index] = updated_student
            return updated_student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")


@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int) -> dict:
    for index, existing_student in enumerate(students_db):
        if existing_student["id"] == student_id:
            students_db.pop(index)
            return {"message": "Student eliminado"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
