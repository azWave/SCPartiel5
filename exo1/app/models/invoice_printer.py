class InvoicePrinter:
    def print_invoice(self, price: float) -> None:
        print(f"Total: {price}")
        if price > 100:
            print("Apply special discount next time!")