
from utilities import get_valid_input


class Property:
    def __init__(self, square_feet='', bedrooms='', bathrooms='', *args, **kwargs):
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display(self):
        print(f'General Information\n'
              f'======================\n'
              f'Square Feet: {self.square_feet}\n'
              f'Bedrooms: {self.bedrooms}\n'
              f'Bathrooms: {self.bathrooms}\n')

    def prompt_init():
        return dict(
            square=input('Square Feet: '),
            bedrooms=input('Bedrooms: '),
            bathrooms=input('Bathrooms: ')
        )

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    def __init__(self, balcony='', laundry='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print(f'Balcony: {self.balcony}\n'
              f'Laundry: {self.laundry}')

    def prompt_init():
        parent_init = Property.prompt_init()

        balcony = get_valid_input(
            'Dose apartment have a balcony? ',
            ('yes', 'no')
        )

        laundry = get_valid_input(
            'What laundry type do you prefer? ',
            ('coin', 'credit_card', 'none')
        )

        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    def __init__(self, number_stories='', garage='', fenced='', pool='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_stories = number_stories
        self.garage = garage
        self.fenced = fenced
        self.pool = pool

    def display(self):
        super().display()
        print(f'Number of Stories: {self.number_stories}\n'
              f'Garage: {self.garage}\n'
              f'Fenced: {self.fenced}\n'
              f'Pool: {self.pool}')

    def prompt_init():
        parent_init = Property.prompt_init()

        number_stories = input('How many stories do you want? ')

        garage = get_valid_input(
            'Do you want to garage? ',
            ('attach', 'detached', 'none')
        )

        pool = get_valid_input(
            'Do you prefer to pool? ',
            ('yes', 'no')
        )

        fenced = get_valid_input(
            'Do you prefer to fenced in your house? ',
            ('ok', 'no')
        )

        parent_init.update({
            'number_stories': number_stories,
            'garage': garage,
            'fenced': fenced,
            'pool': pool
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)
