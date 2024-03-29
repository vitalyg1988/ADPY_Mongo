# Домашнее задание к лекции 2.4 «Database. Mongo. ORM»

1. Вы реализуете приложение для поиска билетов на концерт. Заполните коллекцию в Монго данными о предстоящих концертах и реализуйте следующие функции:

- `read_data`: импорт данных из csv [файла](https://github.com/netology-code/py-homework-advanced/blob/master/2.4.DB.Mongo.ORM/artists.csv)
- `find_cheapest`: отсортировать билеты из базы по возрастания цены
- `find_by_name`: найти билеты по исполнителю, где имя исполнителя может быть задано не полностью, и вернуть их по возрастанию цены


## Дополнительное задание

- Реализовать сортировку по дате мероприятия. Для этого вам потребуется строку с датой в csv-файле приводить к объекту datetime (можете считать, что все они текущего года) и сохранять его.

Пример поиска: найти все мероприятия с 1 по 30 июля.

```python

import csv
import re

from pymongo import MongoClient



def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска. ' \
                       'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать')


if __name__ == '__main__':
    pass
```

Please install requirements.txt

You can use docker-compose.yml for fast run mongo in Docker.
