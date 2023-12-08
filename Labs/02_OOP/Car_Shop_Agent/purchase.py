
from cars import Cars, Automobile, Truck, Electric


class Purchase(Cars):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f'Purchase Details\n'
              f'==================\n'
              f'Price: {self.price}\n'
              f'Taxes: {self.taxes}')

    @staticmethod
    def prompt_init():
        return dict(
            price=input('What is your selling price? '),
            taxes=input('What is your taxes? ')
        )


class AutomobilePurchase(Automobile, Purchase):
    @staticmethod
    def prompt_init():
        init = Automobile.prompt_init()
        init.update(Purchase.prompt_init())

        return init


class TruckPurchase(Truck, Purchase):
    @staticmethod
    def prompt_init():
        init = Truck.prompt_init()
        init.update(Purchase.prompt_init())

        return init


class ElectricPurchase(Electric, Purchase):
    @staticmethod
    def prompt_init():
        init = Electric.prompt_init()
        init.update(Purchase.prompt_init())

        return init
