import json
from hw2 import Advert


def test_one_point_access():
    lesson_str = """{
        "title": "python", "price": 0,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.title == "python"
    assert lesson_ad.price == 0


def test_two_point_access():
    lesson_str = """{
        "title": "python", "price": 0,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    assert lesson_ad.location.metro_stations == ["Белорусская"]


def test_price_negative():
    try:
        lesson_str = '{"title": "python", "price": -1}'
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        lesson_ad
    except ValueError:
        assert 1


def test_no_price():
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


def test_color_output():
    lesson_str = '{"title": "Вельш-ĸорги", "price": 1000}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)


if __name__ == '__main__':
    test_one_point_access()
    test_two_point_access()
    test_price_negative()
    test_no_price()
    test_color_output()
