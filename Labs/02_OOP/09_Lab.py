
from abc import ABC, abstractmethod

# Entities


class CreditCard:
    def __init__(self):
        self.bank_name = ''
        self.card_limit = 0
        self.card_type = ''
        self.installment_shopping = False


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()

    @property
    def credit_card(self) -> CreditCard:
        return self._credit_card

    @abstractmethod
    def bank_name_func(self) -> str: pass

    @abstractmethod
    def card_limit_func(self) -> int: pass

    @abstractmethod
    def card_type_func(self) -> str: pass

    @abstractmethod
    def installment_shopping_func(self) -> bool: pass


class AmericanExpressCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = 'Garanti'
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 500000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = 'American Express'
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping


class VisaCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = 'İş Bankası'
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 500000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = 'Visa Card'
        return self._credit_card.card_type

    def installment_shopping_func(self) -> bool:
        self._credit_card.installment_shopping = True
        return self._credit_card.installment_shopping


class Creator:
    @staticmethod
    def create_credit_card(credit_card_builder: CreditCardBuilder):
        print(f'Bank Name: {credit_card_builder.bank_name_func()}')
        print(f'Card Limit: {credit_card_builder.card_limit_func()}')
        print(f'Card Type: {credit_card_builder.card_type_func()}')
        print(f'Shopping Type: {credit_card_builder.installment_shopping_func()}')


def main():
    Creator.create_credit_card(AmericanExpressCard())
    Creator.create_credit_card(VisaCard())


main()
