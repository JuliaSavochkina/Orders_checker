import xml.etree.ElementTree as ET
from export_csv import export_to_csv


def _keys_check(order: dict) -> None:
    """
    Проверяет наличие всех обязательных ключей (полей) в заказе, если какое-то поле отсутствует, пишет ошибку в csv-файл.
    :param order: словарь с данными по заказу
    :return:
    """
    keys: list = [
        'uid',
        'order_id',
        'tariff_code',
        'action_code',
        'price',
        'quantity',
        'position_count',
        'position_id',
        'product_id',
        'payment_type',
        'currency_code'
    ]
    for key in keys:
        if key not in order.keys():
            try:
                export_to_csv({'Order_id': order["order_id"], 'Error message': f'No key {key}'})
            except KeyError:
                export_to_csv({'Order_id': 'NO order_id', 'Error message': f'for {order}'})


def _values_not_null(order: dict) -> None:
    """
    Проверяет что значения ключей не пусто, если какое-то значение отсутствует, пишет ошибку в csv-файл.
    :param order: словарь с данными по заказу
    :return:
    """
    for key, value in order.items():
        if value is None:
            try:
                export_to_csv({'Order_id': order["order_id"], 'Error message': f'{key} is empty'})
            except KeyError:
                export_to_csv({'Order_id': 'NO order_id', 'Error message': f'for {order}'})


def _uid_length_check(order: dict) -> None:
    """
    Проверяет, что длина uid 32 символа, иначе пишет ошибку в csv-файл.
    :param order: словарь с данными по заказу
    :return:
    """
    try:
        if len(str(order['uid'])) != 32:
            export_to_csv({'Order_id': order["order_id"], 'Error message': f'Unexpected length of uid -'
                                                                           f' {len(str(order["uid"]))} symbol(s)'})
    except KeyError:
        export_to_csv({'Order_id': 'NO order_id', 'Error message': f'for {order}'})


def validate_order(order: dict) -> None:
    """
    Проходит всеми проверками из списка checkers по заказу
    :param order: словарь с данными по заказу
    :return:
    """
    checkers: list = [_keys_check, _values_not_null, _uid_length_check]
    for func in checkers:
        func(order)


if __name__ == '__main__':
    def parse_orders_test() -> dict:
        tree = ET.parse('test_xml')
        root = tree.getroot()
        for child in root:
            order = {}
            for child1 in child:
                order.update({child1.tag: child1.text})
            yield order

    for each in parse_orders_test():
        validate_order(each)
