import unittest
from task_1 import check, f_sum


params_f_sum = ((1, 2, 3),
                (5, 4, 9))


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

    def test_f_sum(self):
        for a, b, expected in params_f_sum:
            with self.subTest(msg=f'При вызове f_sum({a}, {b}) ожидался ответ: {expected}!'):
                result = f_sum(a, b)
                self.assertEquals(result, expected, f'Функция возвращает: {result}')

if __name__ == '__main__':
    unittest.main()
