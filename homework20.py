from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from bson import ObjectId

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@ivanovich287.eqsbsxp.mongodb.net/?appName=ivanovich287"

client = MongoClient(uri, server_api=ServerApi('1'))

databases = client.list_databases()
print(databases)

for db in databases:
    print(db)
db_collection = client.books_collection
collection_books = db_collection['books']

book = {'title': 'Гра престолів', "price": 1050, 'year of graduation': 1996, 'number_of_pages': 800}
# collection_books.insert_one(book)

books = [
    {'title': 'алгебра ', 'class': 7, 'number_of_pages': 60, 'year of graduation': 2022},
    {'title': 'укр мова', 'class': 4, 'number_of_pages': 167, 'year of graduation': 2022},
    {'title': 'біологія', 'class': 8, 'number_of_pages': 143, 'year of graduation': 2022},
    {'title': 'географія', 'class': 9, 'number_of_pages': 136, 'year of graduation': 2022},
    {'title': 'інформатика', 'class': 5, 'number_of_pages': 84, 'year of graduation': 2022},
]

# created_books = collection_books.insert_many(books)
query = {'class': {"$gt": 4, "$lte": 8}}
books_for_5_to_8_class = collection_books.find(query)
for book in books_for_5_to_8_class:
    print(book, 'книжкі з 5 по 8 клас')

query2 = {'year of graduation': 2022}
find_2022_books = collection_books.find(query2).limit(3).sort('class', -1)
for book in find_2022_books:
    print(book, 'книжкі з 2022')
the_book_with_the_most_pages = collection_books.find().limit(1).sort('number_of_pages', -1)
print(list(the_book_with_the_most_pages), 'книжка з найбільшою кількістю сторінок')
