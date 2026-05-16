from storage import load_books

def average_rating():
    books = load_books()
    if not books:
        return 0
    return sum(b.rating for b in books) / len(books)

def stats_by_author():
    books = load_books()
    authors = {}
    for b in books:
        authors.setdefault(b.author, []).append(b.rating)
    return {a: round(sum(r)/len(r), 2) for a, r in authors.items()}