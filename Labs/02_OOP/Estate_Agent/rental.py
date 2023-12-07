
from property import Property, Apartment, House
from utilities import get_valid_input


class Rental(Property):
    def __init__(self, furnished='', extras='', rent='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.furnished = furnished
        self.extras = extras
        self.rent = rent

    def display(self):
        super().display()
        print(f'Rental Detail\n'
              f'=================\n'
              f'Rent: {self.rent}\n'
              f'Furnished: {self.furnished}\n'
              f'Extras: {self.extras}\n')

    def prompt_init():
        return dict(
            furnished=get_valid_input(
                'Has apartment furnished? ',
                ('yes', 'no')
            ),
            extras=input('What are the extras prefer? '),
            rent=input('What is the estimated monthly rental? ')
        )

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Apartment, Rental):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


class HouseRental(House, Rental):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


