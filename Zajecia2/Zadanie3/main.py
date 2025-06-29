from typing import Dict, Optional

"""
Zaprojektuj klasę Library, która przechowuje książki w postaci słownika {ISBN:
title}. Dodaj metodę find_book, która przyjmuje numer ISBN (str) i zwraca tytuł
książki (str) lub None, jeśli książki nie ma w bibliotece. Zastosuj podpowiedzi typów.
"""

class Library:
    def __init__(self) -> None:
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

library = Library()

library.add_book("978-83-7510-123-4", "Wiedźmin: Ostatnie życzenie")
library.add_book("978-83-7023-123-7", "Władca Pierścieni: Drużyna Pierścienia")

print(library.find_book("978-83-7510-123-4"))  # Output: Wiedźmin: Ostatnie życzenie
print(library.find_book("978-83-7023-123-7"))  # Output: Władca Pierścieni: Drużyna Pierścienia
print(library.find_book("978-00-0000-000-0"))  # Output: None
