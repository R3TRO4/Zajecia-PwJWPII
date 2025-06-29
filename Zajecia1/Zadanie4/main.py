
"""
Stwórz hierarchię klas, która modeluje różne rodzaje książek w bibliotece.
Wymagania:
1. Utwórz klasę bazową Ksiazka z atrybutami:
a. tytul (str)
b. autor (str)
c. rok_wydania (int)
d. Metoda opis(), która zwraca podstawowy opis książki.
2. Utwórz klasy dziedziczące:
a. Ebook – dodatkowy atrybut rozmiar_pliku (w MB). Metoda opis()
powinna dodatkowo informować o rozmiarze pliku.
b. Audiobook – dodatkowy atrybut czas_trwania (w minutach). Metoda
opis() powinna zwracać informację o czasie trwania.
3. Test: Utwórz kilka obiektów obu typów i wypisz ich opisy.
"""

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return (f"tytuł: {self.tytul},\n"
                f"autor: {self.autor},\n"
                f"rok wydania: {self.rok_wydania}\n")

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return (f"tytuł: {self.tytul},\n"
                f"autor: {self.autor},\n"
                f"rok wydania: {self.rok_wydania},\n"
                f"rozmiar pliku: {self.rozmiar_pliku} MB\n")

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku
        self.czas_trwania = czas_trwania

    def opis(self):
        return (f"tytuł: {self.tytul},\n"
                f"autor: {self.autor},\n"
                f"rok wydania: {self.rok_wydania},\n"
                f"rozmiar pliku: {self.rozmiar_pliku} MB,\n"
                f"czas trwania: {self.czas_trwania} min\n")

if __name__ == '__main__':

    ksiazka1 = Ksiazka("Lalka", "Bolesław Prus", 1889)
    ksiazka2 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)

    print(ksiazka1.opis())
    print(ksiazka2.opis())

    ebook1 = Ebook("Zbrodnia i Kara", "Fiodor Dostojewski", 1866, 2.5)
    print(ebook1.opis())

    audiobook1 = Audiobook("Hobbit", "J.R.R. Tolkien", 1937, 453, 636)
    print(audiobook1.opis())