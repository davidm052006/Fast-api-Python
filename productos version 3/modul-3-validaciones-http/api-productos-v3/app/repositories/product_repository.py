from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate


class ProductRepository:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def list_all(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)

    def create(self, product_create: ProductCreate) -> Product:
        product = Product(
            id=self.next_id,
            name=product_create.name,
            price=product_create.price,
            stock=product_create.stock,
        )
        self.products[self.next_id] = product
        self.next_id += 1
        return product

    def update(self, product_id: int, product_update: ProductUpdate) -> Product | None:
        product = self.products.get(product_id)
        if product is None:
            return None
        update_data = product_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(product, field, value)
        return product

    def delete(self, product_id: int) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
