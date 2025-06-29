"""Moduł zarządzania prostą biblioteką z wypożyczaniem książek."""


class Ksiazka:
    """Reprezentuje książkę w bibliotece."""

    def __init__(self, tytul, autor, dostepna=True):
        """
        Inicjalizuje obiekt książki.
        :param tytul: Tytuł książki.
        :param autor: Autor książki.
        :param dostepna: Czy książka jest dostępna (domyślnie True).
        """
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna

    def opis(self):
        """
        Zwraca tekstowy opis książki.
        :return: String w formacie "Tytuł – Autor".
        """
        return f"{self.tytul} – {self.autor}"

    def czy_dostepna(self):
        """
        Zwraca True, jeśli książka jest dostępna, False w przeciwnym razie.
        :return: Boolean.
        """
        return self.dostepna


class Biblioteka:
    """Zarządza kolekcją książek i operacjami bibliotecznymi."""

    def __init__(self):
        """Inicjalizuje pustą listę książek w bibliotece."""
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """
        Dodaje książkę do biblioteki.
        :param ksiazka: Obiekt klasy Ksiazka do dodania.
        """
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """
        Wypożycza książkę o podanym tytule, jeśli jest dostępna.
        :param tytul: Tytuł książki do wypożyczenia.
        :return: Komunikat tekstowy z wynikiem operacji.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypożyczono: {tytul}"
                return f"Książka {tytul} niedostępna"
        return f"Brak książki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """
        Zwraca książkę do biblioteki.
        :param tytul: Tytuł książki do zwrotu.
        :return: Komunikat tekstowy z wynikiem operacji.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrócono: {tytul}"
        return f"Nie należy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """
        Zwraca listę tytułów książek aktualnie dostępnych w bibliotece.
        :return: Lista tytułów książek.
        """
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.tytul)
        return dostepne


def main():
    """Funkcja główna testująca działanie biblioteki."""
    biblioteka = Biblioteka()
    ks1 = Ksiazka("Wiedzmin", "Sapkowski")
    ks2 = Ksiazka("Solaris", "Lem")
    ks3 = Ksiazka("Lalka", "Prus", False)

    biblioteka.dodaj_ksiazke(ks1)
    biblioteka.dodaj_ksiazke(ks2)
    biblioteka.dodaj_ksiazke(ks3)

    print(ks1.opis())
    print(f"Dostępna? {ks1.czy_dostepna()}")
    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostępne książki: ", biblioteka.dostepne_ksiazki())


main()
