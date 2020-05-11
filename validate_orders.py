import xml.etree.ElementTree as ET

"""TODO:
* подумать, как реализовать вывод ошибки с указанием номера заказа, если номера нет, подумать. что выводить"""


def _keys_check(order: dict):
    keys = [
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
        if key in order.keys():
            print('ok')
        else:
            print(f'No key "{key}"')


def _values_not_null(order: dict):
    pass


def _uid_check(order: dict):
    pass


def validate_order(order: dict, check: str):
    checkers: dict = {
      'check_keys': _keys_check,
      'check_values': _values_not_null,
      'check_uid': _uid_check
    }

    if check not in checkers:
        print(f'There is no such checker as {check}')
    else:
        checkers.get(order, check)


if __name__ == '__main__':
    def parse_orders_test() -> dict:
        tree = ET.parse('test_xml')
        root = tree.getroot()
        for child in root:
            order = {}
            for child1 in child:
                order.update({child1.tag: child1.text})
            return order

    for each in parse_orders_test():
        print(_keys_check(each))
