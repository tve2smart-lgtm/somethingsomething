import json
import os
from models import Book

FILE = "books.json"

def load_books():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return [Book.from_dict(b) for b in json.load(f)]

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=2)

def add_book(book):
    books = load_books()
    for b in books:
        if b.author == book.author and b.title == book.title:
            print("Такая книга уже есть. Closes #1")
            return
    books.append(book)
    save_books(books)

def delete_book(title):
    books = load_books()
    new_books = [b for b in books if b.title != title]
    if len(new_books) == len(books):
        print("Книга не найдена.")
    else:
        save_books(new_books)
        print("Книга удалена.")