
from purchase import AutomobilePurchase, TruckPurchase, ElectricPurchase
from rental import AutomobileRental, TruckRental, ElectricRental
from utilities import get_valid_input


class Agent:
    def __init__(self):
        self.cars = []

    def display_cars_list(self):
        for car in self.cars:
            car.display()

    process_type = {
        ('automobile', 'purchase'): AutomobilePurchase,
        ('automobile', 'rent'): AutomobileRental,
        ('truck', 'purchase'): TruckPurchase,
        ('truck', 'rent'): TruckRental,
        ('electric', 'purchase'): ElectricPurchase,
        ('electric', 'rent'): ElectricRental,
    }

    def request_car(self):
        car_type = get_valid_input(
            'What type car do you want? ',
            ('automobile', 'truck', 'electric')
        )

        payment_type = get_valid_input(
            'What type payment do you want? ',
            ('purchase', 'rent')
        )

        select_type = self.process_type[car_type, payment_type]
        init_args = select_type.prompt_init()
        self.cars.append(select_type(**init_args))


def main():
    agent = Agent()
    agent.request_car()
    agent.display_cars_list()


main()
