from thread_orders import thread_orders


def main():
    url = input('Ссылка на фид: ')
    thread_orders(url)


if __name__ == "__main__":
    main()