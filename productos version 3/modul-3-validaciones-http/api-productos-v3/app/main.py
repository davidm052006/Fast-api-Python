from fastapi import FastAPI
from app.api.routes.products_routes import router as product_router

app = FastAPI(
    title="API de Productos v3",
    description="Tercera versión: validaciones Pydantic, códigos HTTP correctos y errores estructurados.",
    version="3.0.0"
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de Productos v3!"}

app.include_router(product_router)
