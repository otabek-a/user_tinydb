import csv
from tinydb import TinyDB, Query
import argparse
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


def insert_into_db(data, db_path=None):
    if db_path is None:
        raise ValueError('it not be empty')
    if not data:
        raise ValueError('Data must not be empty')
    db = TinyDB(db_path)
    info = []
    for i in data:
        info.append(db.insert(i))
    return info


def query_db(db_path, query_field=None, query_value=None):
    db = TinyDB(db_path)
    query = Query()
    
    if query_field and query_value:
        if query_field == 'id':
            result = db.search(query.id == query_value)
        elif query_field == 'first_name':
            result = db.search(query.first_name == query_value)
        elif query_field == 'last_name':
            result = db.search(query.last_name == query_value)
        elif query_field == 'email':
            result = db.search(query.email == query_value)
        elif query_field == 'gender':
            result = db.search(query.gender == query_value)
        elif query_field == 'job':
            result = db.search(query.job == query_value)
        else:
            result = []
    else:
        result = db.all()
    
    return result


def main():
    parser = argparse.ArgumentParser(description="Convert CSV data into a TinyDB database.")
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('--db', help='Path to the TinyDB database')

    args = parser.parse_args()

    try:
        data = read_csv(args.csv_file)
        insert_into_db(data, args.db)
        print(f"Data inserted into {args.db} successfully.")
    except :
       raise ValueError('mistake')

if __name__ == "__main__":
    main()



    