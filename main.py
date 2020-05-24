from get_orders import get_orders
from parse_orders import parse_orders
from validate_orders import validate_order

# url = 'https://mytoys.advcake.com/export/admitad?pass=q8q77yzh4IGPYkiHjgGcvBGdbF3Jbh3J'


raw_data = get_orders()
for each in parse_orders(raw_data):
    validate_order(each)
