from views import show_menu, get_rational, get_complex, show_result
from models import parse, calculate


def process_data():
    """ Процесс запроса, обработки и вывода результата """
    number_type = show_menu()
    user_input = ""
    if number_type == 'Q':
        user_input = get_rational()
    else:
        user_input = get_complex()
    data = parse(user_input)
    result = calculate(data)
    show_result(result)
