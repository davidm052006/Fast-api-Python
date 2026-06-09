# Módulo 1 - FastAPI Básico

API REST para la gestión de productos, construida con FastAPI. Cubre los fundamentos de creación de endpoints, modelos con Pydantic y manejo de errores HTTP.

## Tecnologías

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows)
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API quedará disponible en `http://127.0.0.1:8000`  
Documentación interactiva en `http://127.0.0.1:8000/docs`

## Endpoints

### Productos

| Método   | Ruta                    | Descripción                              |
|----------|-------------------------|------------------------------------------|
| `GET`    | `/products/`            | Lista todos los productos                |
| `GET`    | `/products/{id}`        | Obtiene un producto por ID               |
| `POST`   | `/products/`            | Crea un nuevo producto                   |
| `PUT`    | `/products/{id}`        | Actualiza un producto existente          |
| `DELETE` | `/products/{id}`        | Elimina un producto                      |

### Filtro por stock

El endpoint `GET /products/` acepta un query param opcional:

```
GET /products/?min_stock=10
```

Retorna solo los productos con stock mayor o igual al valor indicado.

## Schemas

### ProductCreate / ProductUpdate

```json
{
  "name": "string (1-100 caracteres)",
  "price": "float (mayor a 0)",
  "stock": "int (mayor o igual a 0)"
}
```

### ProductResponse

```json
{
  "id": 1,
  "name": "Producto ejemplo",
  "price": 9.99,
  "stock": 50
}
```

## Estructura del proyecto

```
modulo-1-fastapi-basico/
├── app/
│   ├── main.py        # Definición de rutas y lógica principal
│   └── schemas.py     # Modelos Pydantic para validación
├── .gitignore
├── README.md
└── requirements.txt
```
