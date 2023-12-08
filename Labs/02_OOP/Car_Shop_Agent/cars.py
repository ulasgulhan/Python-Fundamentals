
from utilities import get_valid_input


class Cars:
    def __init__(self, brand='', color='', torque='', *args, **kwargs):
        self.brand = brand
        self.color = color
        self.torque = torque

    def display(self):
        print(f'General Information\n'
              f'=====================\n'
              f'Brand: {self.brand}\n'
              f'Color: {self.color}\n'
              f'Torque: {self.torque}')

    @staticmethod
    def prompt_init():
        return dict(
            brand=input('Brand: '),
            color=input('Color: '),
            torque=input('Torque: '),
        )


class Automobile(Cars):
    def __init__(self, fuel_type='', gearbox='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_type = fuel_type
        self.gearbox = gearbox

    def display(self):
        super().display()
        print(f'Fuel Type: {self.fuel_type}\n'
              f'Gearbox: {self.gearbox}')

    @staticmethod
    def prompt_init():
        parent_init = Cars.prompt_init()

        fuel_type = get_valid_input(
            'What type of fuel do you want? ',
            ('gasoline', 'diesel')
        )

        gearbox = get_valid_input(
            'What type of gearbox do you want? ',
            ('manuel', 'automatic')
        )

        parent_init.update({
            'fuel_type': fuel_type,
            'gearbox': gearbox
        })

        return parent_init


class Truck(Cars):
    def __init__(self, capacity='', length='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = capacity
        self.length = length

    def display(self):
        super().display()
        print(f'Capacity: {self.capacity}\n'
              f'Length: {self.length}')

    @staticmethod
    def prompt_init():
        parent_init = Cars.prompt_init()

        capacity = get_valid_input(
            'How many kilos do you want to carry? ',
            ('500', '1000', '1500')
        )

        length = get_valid_input(
            'What is the length of the vehicle you want? ',
            ('7000', '8000', '9000')
        )

        parent_init.update({
            'capacity': capacity,
            'length': length
        })

        return parent_init


class Electric(Cars):
    def __init__(self, battery_type='', maximum_range='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.battery_type = battery_type
        self.maximum_range = maximum_range

    def display(self):
        super().display()
        print(f'Battery Type: {self.battery_type}\n'
              f'Maximum Range: {self.maximum_range}')

    @staticmethod
    def prompt_init():
        parent_init = Cars.prompt_init()

        battery_type = get_valid_input(
            'What type of battery do you want? ',
            ('standard range', 'long range')
        )

        maximum_range = get_valid_input(
            'What is the maximum distance you want your vehicle to go? ',
            ('440', '600')
        )

        parent_init.update({
            'battery_type': battery_type,
            'maximum_range': maximum_range
        })

        return parent_init
