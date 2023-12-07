
from property import Property, House, Apartment


class Purchase(Property):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f'Purchase Detail\n'
              f'==================\n'
              f'Selling Price: {self.price}\n'
              f'Taxes: {self.taxes}\n')

    def prompt_init():
        return dict(
            price=input('What is the selling price: '),
            taxes=input('What is the estimated taxes: ')
        )

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Apartment, Purchase):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(House, Purchase):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)

