from click.testing import CliRunner
from cli import cli
from certain_pizzas import Margherita, Pepperoni, Hawaiian


def test_pizzas_menu():
    runner = CliRunner()
    result = runner.invoke(cli, ["menu"])
    assert result.exit_code == 0
    assert result.output == "- Margherita 🧀: tomato sauce, "\
        "mozzarella, tomatoes\n"\
        "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n"\
        "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n"


def test_Margherita_receipt():
    out = Margherita().dict()
    assert out == "- Margherita 🧀: tomato sauce, mozzarella, tomatoes"


def test_Hawaiian_receipt():
    out = Hawaiian().dict()
    assert out == "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples"


def test_Pepperoni_receipt():
    out = Pepperoni().dict()
    assert out == "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni"


def test_order_with_pickup():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni"])
    assert result.exit_code == 0
    assert result.output.startswith("bake -")
    assert result.output.split('\n')[1].startswith("🛵 Забрали за ")


def test_order_with_delivery():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "pepperoni", "--delivery"])
    assert result.exit_code == 0
    assert result.output.startswith("bake -")
    assert result.output.split('\n')[1].startswith("🏠 Доставили за ")


def test_order_unknown():
    runner = CliRunner()
    result = runner.invoke(cli, ["order", "4 cheese", "--delivery"])
    assert result.exit_code != 0


def test_eq():
    assert Margherita() == Margherita()
    assert not (Margherita() == Hawaiian())
    assert not (Margherita() == Pepperoni())
    assert Hawaiian() == Hawaiian()
    assert not (Hawaiian() == Pepperoni())
    assert Pepperoni() == Pepperoni()
