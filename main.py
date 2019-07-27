import csv
import re
import os

from pymongo import MongoClient


def init_db():
    client = MongoClient('localhost', 27017, username='root', password='pass')
    netology_db = client['netology']
    return netology_db


def read_data(csv_file):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            row['Цена'] = int(row['Цена'])
            rows.append(row)
        return rows


def find_cheapest(db_collection):
    return db_collection.find().sort('Цена', 1)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """
    s_pat = '%s*' % (name, )
    pattern = re.compile(s_pat, re.I)
    return db.find({'Исполнитель': {'$regex': pattern}}).sort('Цена', 1)


if __name__ == '__main__':
    data_file_path = os.path.join(os.path.abspath('.'), 'artists.csv')

    db = init_db()
    data_coll = db.get_collection('artist')

    if data_coll.estimated_document_count() == 0:
        data = read_data(data_file_path)
        data_coll.insert_many(data)

    print('By NAME')
    by_name_data = find_by_name('ри', data_coll)

    for doc in by_name_data:
        print(doc)

    print('CHEAPEST')

    cheapest = find_cheapest(data_coll)

    for doc in cheapest:
        print(doc)
