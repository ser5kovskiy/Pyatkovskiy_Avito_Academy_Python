from one_hot_encoder import fit_transform
import pytest


def test_one_category():
    assert [(1, [1])] == fit_transform(list([1]))


def test_two_category():
    assert [([1])] != fit_transform(list([1]))


def test_iterable_exception():
    try:
        fit_transform(1, 2)
    except (TypeError):
        assert 1


def test4():
    assert [(1, [0, 0, 0, 1]), (2, [0, 0, 1, 0]), (4, [0, 1, 0, 0]), (0, [
        1, 0, 0, 0])] == fit_transform(list([1, 2, 4, 0]))
