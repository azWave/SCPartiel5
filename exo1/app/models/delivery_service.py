from models.package import Package
from models.pricing import PricingStrategy
from models.discount import DiscountStrategy

class DeliveryService:
    def __init__(self, pricing_strategy: PricingStrategy, discount_strategy: DiscountStrategy):
        self.pricing_strategy = pricing_strategy
        self.discount_strategy = discount_strategy

    def calculate_delivery_price(self, packages: list[Package]) -> float:
        total = sum(self.pricing_strategy.calculate_price(pkg) for pkg in packages)
        total = self.discount_strategy.apply_discount(total)

        if len(packages) > 3:
            total *= 0.95  
        
        return total