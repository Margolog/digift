from dataclasses import dataclass
from typing import List

@dataclass()
class Product:
    name: str
    image: str
    price: float

@dataclass()
class JsTestTask:
    def __init__(self, products: List[Product]):
        self.products = products



