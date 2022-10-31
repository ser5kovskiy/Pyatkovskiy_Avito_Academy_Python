import click
from certain_pizzas import Margherita, Pepperoni, Hawaiian
import func_pr

pizzas_names = {"margherita": Margherita,
                "pepperoni": Pepperoni, "hawaiian": Hawaiian}


@click.group()
def cli():
    pass


@cli.command()
@click.argument("pizza", nargs=1)
@click.argument("size", default="L")
@click.option("--delivery", default=False, is_flag=True)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza_cur_name = pizza.lower()
    func_pr.bake(pizzas_names[pizza_cur_name](size=size))
    if (delivery):
        func_pr.delivery(pizzas_names[pizza_cur_name]())
    else:
        func_pr.pickup(pizzas_names[pizza_cur_name]())


@cli.command()
def menu():
    """Выводит меню"""
    for cur_pizza_name, cur_pizza_class in pizzas_names.items():
        print(cur_pizza_class().dict())


if __name__ == '__main__':
    cli()
