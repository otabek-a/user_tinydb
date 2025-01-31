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



if __name__ == "__main__":
    # Main execution logic
    pass