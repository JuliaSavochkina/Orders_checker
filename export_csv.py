import csv


def export_to_csv(message: dict):
    with open('error_log.csv', "a", newline='') as file:
        fieldnames = ['Order_id', 'Error message']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(message)


if __name__ == '__main__':
    error_message = {'Order_id': '123456', 'Error message': 'product_id is empty'}
    export_to_csv(error_message)
