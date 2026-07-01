from fastapi import APIRouter, HTTPException, Response, status
from app.error_responses import error_response
from app.exceptions import ProductNotFoundException, ProductAlreadyExistsException
from app.services.product_service import ProductService
from app.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.repositories.product_repository import ProductRepository

router = APIRouter(prefix="/products", tags=["products"])

repository = ProductRepository()
service = ProductService(repository)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_create: ProductCreate):
    try:
        product = service.create(product_create)
        return ProductResponse(**product.__dict__)
    except ProductAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error_response("PRODUCT_ALREADY_EXISTS", str(e)),
        )


@router.get("", response_model=list[ProductResponse])
def list_products():
    products = service.list_all()
    return [ProductResponse(**product.__dict__) for product in products]


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    try:
        product = service.get_by_id(product_id)
        return ProductResponse(**product.__dict__)
    except ProductNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response("PRODUCT_NOT_FOUND", "El producto solicitado no existe"),
        )


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate):
    update_data = product_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response("EMPTY_UPDATE_BODY", "Debe enviar al menos un campo para actualizar"),
        )
    try:
        updated_product = service.update(product_id, product_update)
        return ProductResponse(**updated_product.__dict__)
    except ProductNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response("PRODUCT_NOT_FOUND", "El producto solicitado no existe"),
        )
    except ProductAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error_response("PRODUCT_ALREADY_EXISTS", str(e)),
        )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    try:
        service.delete(product_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ProductNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response("PRODUCT_NOT_FOUND", "El producto solicitado no existe"),
        )
