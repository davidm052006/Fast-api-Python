# Pruebas - API Productos v3
## Validación, errores y respuestas HTTP en FastAPI

Servidor: `http://127.0.0.1:8000`  
Swagger: `http://127.0.0.1:8000/docs`

---

## Prueba 1 — Crear producto válido → 201 Created

```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name":"Mouse Logitech","price":85000,"stock":20}'
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Mouse Logitech",
  "price": 85000.0,
  "stock": 20,
  "active": true
}
```

---

## Prueba 2 — Nombre inválido → 422 Unprocessable Entity

```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name":"test","price":85000,"stock":20}'
```

**Respuesta esperada:**
```json
{
  "detail": [
    {
      "msg": "Value error, El nombre del producto no está permitido"
    }
  ]
}
```

---

## Prueba 3 — Precio inválido → 422 Unprocessable Entity

```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name":"Monitor","price":0,"stock":20}'
```

**Respuesta esperada:**
```json
{
  "detail": [
    {
      "msg": "Input should be greater than 0"
    }
  ]
}
```

---

## Prueba 4 — Producto duplicado → 409 Conflict

**Primer registro:**
```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name":"Teclado Mecanico","price":250000,"stock":8}'
```

**Segundo registro con el mismo nombre:**
```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name":"Teclado Mecanico","price":260000,"stock":5}'
```

**Respuesta esperada:**
```json
{
  "detail": {
    "error": {
      "code": "PRODUCT_ALREADY_EXISTS",
      "message": "Producto con nombre 'Teclado Mecanico' ya existe."
    }
  }
}
```

---

## Prueba 5 — Producto inexistente → 404 Not Found

```bash
curl -X GET "http://127.0.0.1:8000/products/999"
```

**Respuesta esperada:**
```json
{
  "detail": {
    "error": {
      "code": "PRODUCT_NOT_FOUND",
      "message": "El producto solicitado no existe"
    }
  }
}
```

---

## Prueba 6 — Actualizar con JSON vacío → 400 Bad Request

```bash
curl -X PATCH "http://127.0.0.1:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Respuesta esperada:**
```json
{
  "detail": {
    "error": {
      "code": "EMPTY_UPDATE_BODY",
      "message": "Debe enviar al menos un campo para actualizar"
    }
  }
}
```

---

## Prueba 7 — Actualizar producto correctamente → 200 OK

```bash
curl -X PATCH "http://127.0.0.1:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{"price":90000,"stock":15}'
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Mouse Logitech",
  "price": 90000.0,
  "stock": 15,
  "active": true
}
```

---

## Prueba 8 — Eliminar producto existente → 204 No Content

```bash
curl -X DELETE "http://127.0.0.1:8000/products/1"
```

**Respuesta esperada:** sin cuerpo, código 204.

---

## Prueba 9 — Eliminar producto inexistente → 404 Not Found

```bash
curl -X DELETE "http://127.0.0.1:8000/products/999"
```

**Respuesta esperada:**
```json
{
  "detail": {
    "error": {
      "code": "PRODUCT_NOT_FOUND",
      "message": "El producto solicitado no existe"
    }
  }
}
```

---

## Resumen de resultados

| # | Prueba | Código esperado | Código obtenido |
|---|---|---|---|
| 1 | Crear producto válido | 201 | 201 ✅ |
| 2 | Nombre inválido (`test`) | 422 | 422 ✅ |
| 3 | Precio inválido (`0`) | 422 | 422 ✅ |
| 4 | Producto duplicado | 409 | 409 ✅ |
| 5 | Producto inexistente GET | 404 | 404 ✅ |
| 6 | Actualizar con body vacío | 400 | 400 ✅ |
| 7 | Actualizar correctamente | 200 | 200 ✅ |
| 8 | Eliminar existente | 204 | 204 ✅ |
| 9 | Eliminar inexistente | 404 | 404 ✅ |
