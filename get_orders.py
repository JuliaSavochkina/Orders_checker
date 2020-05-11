import requests

"""TODO:
подумать о переносе ввода фида"""


# url = input('Ссылка на фид: ')
def get_orders() -> str:
    try:
        r = requests.get('https://mytoys.advcake.com/export/admitad?pass=q8q77yzh4IGPYkiHjgGcvBGdbF3Jbh3J')
        return r.text
    except requests.exceptions.RequestException as error:
        print(error)


if __name__ == '__main__':
    # url = 'https://mytoys.advcake.com/export/admitad?pass=q8q77yzh4IGPYkiHjgGcvBGdbF3Jbh3J'
    print(get_orders)
