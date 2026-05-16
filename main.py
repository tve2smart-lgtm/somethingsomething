from models import Book
from storage import add_book, delete_book, load_books
from stats import average_rating, stats_by_author
from datetime import date

def show_all():
    books = load_books()
    if not books:
        print("Список пуст.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b.title} — {b.author} | Оценка: {b.rating} | Дата: {b.date}")

def menu():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            author = input("Автор: ").strip()
            title = input("Название: ").strip()
            rating = int(input("Оценка (1-5): ").strip())
            d = input(f"Дата прочтения (Enter = сегодня {date.today()}): ").strip()
            if not d:
                d = str(date.today())
            add_book(Book(author, title, rating, d))
            print("Книга добавлена.")
        elif choice == "2":
            show_all()
        elif choice == "3":
            print(f"Средняя оценка: {round(average_rating(), 2)}")
        elif choice == "4":
            for author, avg in stats_by_author().items():
                print(f"{author}: {avg}")
        elif choice == "5":
            title = input("Название книги для удаления: ").strip()
            delete_book(title)
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    menu()