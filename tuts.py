
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages


    def __str__(self):
        return f"{self.title} napisano przez {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return  f"{self.num_pages + other.num_pages} stron lacznie"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key =="author":
            return self.author
        elif key =="num_pages":
            return self.num_pages
        else:
            return f"{key} nieznaleziony"



book1 = Book("Hobbit", "J.R.R Tolkien", 310)
book4 = Book("Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "Rowling", 231)
book3 = Book("Pan Kleks","Jan Brzechwa", 112)

print(book1)
print(book2)
print(book3)
print(book1 == book4)

print("Czy ksiazka 1 ma wiecej stron niz ksiazka 2? ", book2 < book1)
print("Czy ksiazka 1 ma mniej stron niz ksiazka 2? ", book2 > book1)
print(book1 + book3)

print("Hobbit" in book2)

print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["kiwi"])