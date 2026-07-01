from app.exceptions import ProductNotFoundException, ProductAlreadyExistsException
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_by_id(self, product_id: int) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ProductNotFoundException(f"Producto con el id #{product_id} no fue encontrado.")
        return product

    def list_all(self) -> list[Product]:
        return self.repository.list_all()

    def _product_exists_by_name(self, name: str) -> bool:
        return any(p.name.lower() == name.lower() for p in self.repository.list_all())

    def create(self, product_data: ProductCreate) -> Product:
        if self._product_exists_by_name(product_data.name):
            raise ProductAlreadyExistsException(f"Producto con nombre '{product_data.name}' ya existe.")
        return self.repository.create(product_data)

    def update(self, product_id: int, product_update: ProductUpdate) -> Product:
        existing_product = self.repository.get_by_id(product_id)
        if existing_product is None:
            raise ProductNotFoundException(f"Producto con el id #{product_id} no fue encontrado.")

        update_data = product_update.model_dump(exclude_unset=True)
        new_name = update_data.get("name")
        if new_name and new_name.lower() != existing_product.name.lower():
            if self._product_exists_by_name(new_name):
                raise ProductAlreadyExistsException(f"Producto con nombre '{new_name}' ya existe.")

        updated_product = self.repository.update(product_id, product_update)
        if updated_product is None:
            raise ProductNotFoundException(f"Producto con el id #{product_id} no fue encontrado.")
        return updated_product

    def delete(self, product_id: int) -> None:
        if not self.repository.delete(product_id):
            raise ProductNotFoundException(f"Producto con el id #{product_id} no fue encontrado.")
