from basic_pizza import BasicPizza


class Margherita(BasicPizza):
    def __init__(self, size="L"):
        self.__name__ = "Margherita"
        self.__receipt__ = "tomato sauce, mozzarella, tomatoes"
        self.size = size
        self.emoji = "🧀"


class Pepperoni(BasicPizza):
    def __init__(self, size="L"):
        self.__name__ = "Pepperoni"
        self.__receipt__ = "tomato sauce, mozzarella, pepperoni"
        self.size = size
        self.emoji = "🍕"


class Hawaiian(BasicPizza):
    def __init__(self, size="L"):
        self.__name__ = "Hawaiian"
        self.__receipt__ = "tomato sauce, mozzarella, chicken, pineapples"
        self.size = size
        self.emoji = "🍍"
