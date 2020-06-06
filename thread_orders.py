from concurrent.futures import ThreadPoolExecutor, as_completed
from get_orders import get_orders
from parse_orders import parse_orders
from validate_orders import validate_order


def thread_orders(url: str, number_of_workers: int = 10) -> None:
    """
    Функция забирает данные из фида, парсит их и валидирует. В несколько потоков.
    :param url: ссылка на фид
    :param number_of_workers: количестов потоков. По умолчанию 10. Можно изменить в main
    :return: None
    """
    with ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        raw_data: str = get_orders(url)
        future_objs: list = [executor.submit(validate_order, each) for each in parse_orders(raw_data)]
