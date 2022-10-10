from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoding(unittest.TestCase):

    def test_one_category(self):
        self.assertEqual([(1, [1])], fit_transform(list([1])))

    def test_two_category(self):
        self.assertNotIn([([1])], fit_transform(list([1])))

    def test_iterable_exception(self):
        try:
            fit_transform(1, 2)
        except (TypeError):
            assert 1

    def test4(self):
        self.assertEqual([(1, [0, 0, 0, 1]), (2, [0, 0, 1, 0]), (4, [0, 1, 0, 0]), (0, [
                         1, 0, 0, 0])], fit_transform(list([1, 2, 4, 0])))


if __name__ == '__main__':
    unittest.main()
