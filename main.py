import random
from typing import List
from decimal import Decimal


class NoMoneyError(Exception):
    pass


class Product:
    def __init__(self, title: str, price: Decimal) -> None:
        super().__init__()
        self.title = title
        self.price = price

    @staticmethod
    def get_random_product() -> 'Product':
        return Product(title=f'Product {random.randint(1, 100)}', price=Decimal(random.randint(100, 1000)))


class House(Product):
    def __init__(self, square: float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.square = square

    @staticmethod
    def get_random_product() -> 'House':
        return House(
            title=f'House {random.randint(1, 100)}',
            price=Decimal(random.randint(100, 1000)),
            square=random.randint(100, 1000),
        )

    def has_garage(self) -> bool:
        return self.square > 100


class Car(Product):
    def __init__(self, energy: float = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.energy = energy or random.random() * 100


class Human:
    def __init__(self, name: str, age: int, money: Decimal) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.money = money

    def can_buy(self, product: Product) -> bool:
        if isinstance(product, House) and self.age < 30:
            return False

        if isinstance(product, Car) and self.age <= 20:
            return False

        return True


class Agency:
    def get_products(self) -> List[Product]:
        houses = []
        for _ in range(10):
            houses.append(House.get_random_product())

        cars = [Car.get_random_product() for house in houses if house.has_garage()]
        return houses + cars

    def find_products_to_buy(self, human: Human) -> List[Product]:
        return list(filter(lambda p: human.can_buy(p), self.get_products()))

    def buy(self, human: Human, product: Product) -> None:
        if human.money < product.price:
            raise NoMoneyError()

        print('{name} buy {title} for {price:.02f}'.format(name=human.name, title=product.title, price=product.price))


if __name__ == '__main__':
    agency = Agency()
    human = Human('Vasya', age=25, money=Decimal(500))

    for product in agency.find_products_to_buy(human):
        try:
            agency.buy(human, product)
        except NoMoneyError as exc:
            print(f'{human.name} cannot buy {product.title}')
