from app.models.product import Product
from app.schemas import ProductCreate

class ProductRepository:
    def __init__(self):
        self.products = {}
        self.next_id = 1
    
    def list_all(self) -> list[Product]:
        return list(self.products.values())
    
    def create(self, product_create: ProductCreate) -> Product:
        product = Product(
            id=self.next_id,
            name=product_create.name,
            price=product_create.price,
            stock=product_create.stock
        )
        self.products[self.next_id] = product
        self.next_id += 1
        return product
    
    def update(self, product_id: int, product_update: ProductCreate) -> Product | None:
        product = self.products.get(product_id)
        if product is None:
            return None
        product.name = product_update.name
        product.price = product_update.price
        product.stock = product_update.stock
        return product
    
    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)
    
    def delete(self, product_id: int) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
