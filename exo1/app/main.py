from models.delivery_service import DeliveryService
from models.invoice_printer import InvoicePrinter
from models.package import Package 
from models.pricing import UrgentPricing
from models.discount import VIPDiscount

packages = [Package(6, 100), Package(12, 50), Package(8, 200)]
pricing_strategy = UrgentPricing()
discount_strategy = VIPDiscount()

service = DeliveryService(pricing_strategy, discount_strategy)
price = service.calculate_delivery_price(packages)

invoice = InvoicePrinter()
invoice.print_invoice(price)
