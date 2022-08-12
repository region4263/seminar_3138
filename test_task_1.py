import unittest
from task_1 import check


class Task1Test(unittest.TestCase):
    params = ((5, 25, True),
              (4, 16, True),
              (25, 5, True),
              (8, 9, False))

    def test_check(self):
        for a, b, expected in self.params:
            with self.subTest(msg=f'При вызове check({a}, {b}) ожидался ответ: {expected}!'):
                result = check(a, b)
                self.assertEqual(result, expected, f'Функция возвращает: {result}')


if __name__ == '__main__':
    unittest.main()
