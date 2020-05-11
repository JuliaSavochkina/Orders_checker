import xml.etree.ElementTree as ET
from get_orders import get_orders


def parse_orders(raw_data: str) -> dict:
    root = ET.fromstring(raw_data)
    for child in root:
        order = {}
        for child1 in child:
            order.update({child1.tag: child1.text})
        yield order


if __name__ == '__main__':
    raw_data = get_orders()
    for each in parse_orders(raw_data):
        print(each)
