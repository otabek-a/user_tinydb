import csv
from tinydb import TinyDB, Query

import csv

def read_csv(file_path):
    data = []
    try:
        file = open(file_path, mode='r', newline='')
        reader = csv.DictReader(file)
        for i in reader:
            data.append(i)
        file.close()
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found")
    return data


def insert_into_db(data, db_path):
    if not data:
        raise ValueError('Data must not be empty')
    db = TinyDB(db_path)
    info = []
    for i in data:
        info.append(db.insert(i))
    return info


def query_db(db_path, query_field, query_value):
    # Query the database
    pass

if __name__ == "__main__":
    # Main execution logic
    pass