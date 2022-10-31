from abc import abstractmethod


class BasicPizza():
    def dict(self):
        return ("- {name} {emoji}: {receipt}".format(
            name=self.__name__, emoji=self.emoji, receipt=self.__receipt__))

    def __eq__(self, another_item):
        return (self.size == another_item.size
                and self.dict() == another_item.dict())
