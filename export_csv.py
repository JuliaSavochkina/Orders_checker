import csv


def export_to_csv(message: list):
    with open('error_log.csv', "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(message)


if __name__ == '__main__':
    error_message = ["No key 'uid' for {'order_id': 'myToys.ru-121513935', 'tariff_code': '1'}"]
    export_to_csv(error_message)
