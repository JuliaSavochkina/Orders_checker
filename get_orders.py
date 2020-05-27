import requests
from export_csv import export_to_csv


def get_orders(url: str) -> str:
    """
    Обращается к xml файлу и забирает данные.
    :param url: адрес файла
    :return: все заказы из файла
    """
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.RequestException as error:
        export_to_csv([f'{error}'])


if __name__ == '__main__':
    url = 'https://mytoys.advcake.com/export/admitad?pass=q8q77yzh4IGPYkiHjgGcvBGdbF3Jbh3J'
    print(get_orders(url))
