from certain_pizzas import Margherita
from functools import wraps
from random import randint


def log(input):
    if (isinstance(input, str)):
        def decorator(func):
            def wrapper(*args, **kwargs):
                time_spent = randint(1, 100)
                func(*args, **kwargs)
                print(input.format(time_spent))
            return wrapper
        return decorator
    else:
        @wraps(input)
        def wrapper(*args, **kwargs):
            time_spent = randint(1, 100)
            print(
                "{function_name} - {time}c".format(
                    function_name=input.__name__, time=time_spent))
        return wrapper


@log
def bake(pizza):
    """Готовит Пиццу"""


@log('🛵 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""


@log('🏠 Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""


if __name__ == "__main__":
    bake(Margherita())
    pickup(Margherita())
    delivery(Margherita())
