
from purchase import ApartmentPurchase, HousePurchase
from rental import ApartmentRental, HouseRental
from utilities import get_valid_input


class Agent:
    def __init__(self):
        self.properties = []

    def display_property_list(self):
        for item in self.properties:
            item.display()

    process_type = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase,
    }

    def request_property(self):
        property_type = get_valid_input(
            'What type of property do you want? ',
            ('house', 'apartment')
        )

        payment_type = get_valid_input(
            'What payment type do you prefer? ', ('purchase', 'rental')
        )

        generated_class = self.process_type[(property_type, payment_type)]
        init_args = generated_class.prompt_init()
        self.properties.append(generated_class(**init_args))


agent = Agent()
agent.request_property()
agent.display_property_list()
