import unittest
from calculator.models import parse, calculate


class Task44Test(unittest.TestCase):
    params = {
        1: (
            ('25/5+5', [25.0, '/', 5.0, '+', 5.0]),
            ('25*5-5*2.6', [25.0, '*', 5.0, '-', 5.0, '*', 2.6]),
            ('1.25+5/10', [1.25, '+', 5.0, '/', 10.0]),
            ('6/10*10-10', [6.0, '/', 10.0, '*', 10.0, '-', 10.0])
        ),
        2: (
            ([25.0, '/', 5.0, '+', 5.0], 10.0),
            ([25.0, '*', 5.0, '-', 5.0, '*', 2.6], 125.0 - 5.0 * 2.6),
            ([6.0, '/', 10.0, '*', 10.0, '-', 10.0], -4.0)
        )
    }
    

    def test_parse(self):
        for expression, expected in self.params.get(1):
            with self.subTest(msg=f'При вызове parse({expression}) ожидался ответ: {expected}!'):
                result = parse(expression)
                self.assertEqual(result, expected, f'Функция возвращает: {result}')
    
    def test_calculate(self):
        for data, expected in self.params.get(2):
            with self.subTest(msg=f'При вызове calculate({data}) ожидался ответ: {expected}!'):
                result = calculate(data)
                self.assertEqual(result, expected, f'Функция возвращает: {result}')


if __name__ == '__main__':
    unittest.main()
