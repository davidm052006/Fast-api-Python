# Módulo 2 - Arquitectura en Capas con FastAPI

Este módulo introduce el concepto de **arquitectura en capas** aplicado a una API REST construida con FastAPI. El objetivo es separar las responsabilidades del código en distintas capas para lograr un proyecto más organizado, mantenible y escalable.

---

## Proyecto: `api-productos-v2`

Segunda versión de la API de Productos. A diferencia del módulo anterior (donde todo el código vivía en un solo archivo), aquí se divide la lógica en capas bien definidas.

### Estructura del proyecto

```
api-productos-v2/
├── requirements.txt
└── app/
    ├── main.py
    ├── schemas.py
    ├── exceptions.py
    ├── api/
    │   └── routes/
    │       └── products_routes.py
    ├── models/
    │   └── product.py
    ├── repositories/
    │   └── product_repository.py
    └── services/
        └── product_service.py
```

---

## Descripción de cada capa y archivo

### `main.py`
Punto de entrada de la aplicación. Crea la instancia de `FastAPI` con título, descripción y versión, y registra el router de productos.

### `schemas.py`
Define los modelos de entrada y salida usando **Pydantic**:
- `ProductCreate` — datos requeridos para crear un producto (name, price, stock).
- `ProductUpdate` — datos para actualizar un producto, incluye el campo `active`.
- `ProductResponse` — forma en que se devuelve un producto al cliente.

### `exceptions.py`
Excepciones personalizadas del dominio:
- `ProductNotFoundException` — se lanza cuando no se encuentra un producto por su ID.
- `ProductAlreadyExistsException` — se lanza cuando ya existe un producto con el mismo nombre.
- `InvalidProductDataException` — reservada para validaciones de datos inválidos.

### `models/product.py`
Define la entidad de negocio `Product` usando un **dataclass** de Python. Representa cómo se almacena un producto internamente (id, name, price, stock, active).

### `repositories/product_repository.py`
Capa de **acceso a datos**. Gestiona el almacenamiento en memoria (diccionario) y expone métodos CRUD:
- `list_all()` — retorna todos los productos.
- `get_by_id(id)` — busca un producto por ID.
- `create(data)` — crea y almacena un nuevo producto.
- `update(id, data)` — actualiza los campos de un producto existente.
- `delete(id)` — elimina un producto y retorna `True` si existía.

### `services/product_service.py`
Capa de **lógica de negocio**. Orquesta las operaciones usando el repositorio y aplica las reglas del dominio:
- Verifica que no existan duplicados por nombre antes de crear o actualizar.
- Lanza las excepciones personalizadas cuando corresponde.
- Actúa como intermediario entre las rutas y el repositorio.

### `api/routes/products_routes.py`
Capa de **presentación / controladores**. Define los endpoints REST:

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/products` | Lista todos los productos |
| `GET` | `/products/{id}` | Obtiene un producto por ID |
| `POST` | `/products` | Crea un nuevo producto |
| `PATCH` | `/products/{id}` | Actualiza un producto existente |
| `DELETE` | `/products/{id}` | Elimina un producto |

Convierte las excepciones de dominio en respuestas HTTP con el código de estado apropiado (400, 404, 204, etc.).

---

## Cómo ejecutar

```bash
cd api-productos-v2
pip install -r requirements.txt
fastapi dev app/main.py
```

La documentación interactiva estará disponible en `http://127.0.0.1:8000/docs`.

---

## Concepto clave: ¿Por qué arquitectura en capas?

| Capa | Responsabilidad |
|------|----------------|
| **Routes** | Recibir peticiones HTTP y devolver respuestas |
| **Service** | Aplicar reglas de negocio |
| **Repository** | Acceder y persistir datos |
| **Models** | Representar las entidades del dominio |
| **Schemas** | Validar y serializar datos de entrada/salida |

Cada capa solo se comunica con la capa inmediatamente inferior, lo que facilita el testeo, el mantenimiento y la sustitución de componentes (por ejemplo, cambiar el almacenamiento en memoria por una base de datos real solo requiere modificar el repositorio).
