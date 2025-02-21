from typing import Dict


class Stock:
    def __init__(self, stock: Dict[str, int]):
        self.stock = stock
    
    def has_sufficient_stock(self, medication: str, doses: int, is_weekend: bool) -> bool:
        stock_minimum = 3 * (1.2 if is_weekend else 1)
        return self.stock.get(medication, 0) - doses >= stock_minimum
