
from cars import Cars, Automobile, Truck, Electric
from utilities import get_valid_input


class Rental(Cars):
    def __init__(self, rent_daily='', time='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rent_daily = rent_daily
        self.time = time

    def display(self):
        super().display()
        print(f'Rental Details\n'
              f'================\n'
              f'Daily Rent: {self.rent_daily}\n'
              f'Time: {self.time}')

    @staticmethod
    def prompt_init():
        return dict(
            rent_daily=input('Daily Rent? '),
            time=get_valid_input(
                'Time? ',
                ('daily', 'weekly')
            )
        )


class AutomobileRental(Automobile, Rental):
    @staticmethod
    def prompt_init():
        init = Automobile.prompt_init()
        init.update(Rental.prompt_init())

        return init


class TruckRental(Truck, Rental):
    @staticmethod
    def prompt_init():
        init = Truck.prompt_init()
        init.update(Rental.prompt_init())

        return init


class ElectricRental(Electric, Rental):
    @staticmethod
    def prompt_init():
        init = Electric.prompt_init()
        init.update(Rental.prompt_init())

        return init
