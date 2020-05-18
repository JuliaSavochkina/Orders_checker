import csv


def export_to_csv(massage: list):
    with open('error_log.csv', "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(massage)


if __name__ == '__main__':
    error_massage = ["No key 'uid' for {'order_id': 'myToys.ru-121513935', 'tariff_code': '1'}"]
    export_to_csv(error_massage)
