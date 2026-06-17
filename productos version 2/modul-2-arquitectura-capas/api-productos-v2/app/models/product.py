from dataclasses import dataclass

@dataclass # Define a data class for Product
class Product:
    id: int
    name: str
    stock: int
    price: float
    active: bool = True # Default value for active is True
