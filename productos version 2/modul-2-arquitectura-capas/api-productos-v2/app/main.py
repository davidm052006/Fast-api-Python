from fastapi import FastAPI
from app.api.routes.products_routes import router as product_router

app = FastAPI(
    title="Segunda versión de API de Productos",
    description="Esta es la segunda versión de la API de Productos, con mejoras y nuevas funcionalidades.",
    version="2.0.0"
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de Productos v2!"}

app.include_router(product_router)
