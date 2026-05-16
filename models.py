from dataclasses import dataclass

@dataclass
class Book:
    author: str
    title: str
    rating: int
    date: str

    def to_dict(self):
        return {"author": self.author, "title": self.title, "rating": self.rating, "date": self.date}

    @staticmethod
    def from_dict(data):
        return Book(data["author"], data["title"], data["rating"], data["date"])