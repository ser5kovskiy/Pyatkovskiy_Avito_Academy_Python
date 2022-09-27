class JsonToObj:
    def __init__(self, data):
        for key, val in data.items():
            if isinstance(val, dict):
                setattr(self, key, JsonToObj(val))
            else:
                setattr(self, key, val)


class ColorizeMixin:
    def __str__(self):
        return f"\033[1;{self.repr_color_code};40m {self.title}" \
            f" | {self.price} ₽"


class Advert(ColorizeMixin, JsonToObj):
    repr_color_code = 32

    def __init__(self, json_info):
        if (not ("title" in json_info.keys())):
            raise KeyError("No mandatory \"title\" key")
        super().__init__(json_info)

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"

    def __setattr__(self, key, value):
        if (key == 'price' and value < 0):
            raise ValueError("ValueError: key value must be >= 0")
        self.__dict__[key] = value

    @property
    def price(self):
        try:
            return self.__dict__["price"]
        except Exception:
            return 0
