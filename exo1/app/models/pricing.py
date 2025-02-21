from abc import ABC, abstractmethod
from models.package import Package


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, package: Package) -> float:
        pass


class StandardPricing(PricingStrategy):
    def calculate_price(self, package: Package) -> float:
        base = package.distance * 0.1
        if package.weight > 10:
            base += 5
        elif package.weight > 5:
            base += 3
        return base

class UrgentPricing(PricingStrategy):
    def calculate_price(self, package: Package) -> float:
        return StandardPricing().calculate_price(package) * 1.5