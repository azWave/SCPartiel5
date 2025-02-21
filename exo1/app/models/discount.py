from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.8

class BusinessDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.9