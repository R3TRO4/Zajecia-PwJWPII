class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."

class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, zarządzam zespołem {len(self.zespol)} osób."

    def dodaj_do_zespolu(self, pracownik):
        if isinstance(pracownik, Pracownik):
            self.zespol.append(pracownik)
        else:
            raise TypeError("Do zespołu można dodać tylko pracowników")

if __name__ == '__main__':
    pracownik1 = Pracownik("Jan", "Kowalski", 30, "Inżynier", 8000)
    pracownik2 = Pracownik("Anna", "Nowak", 28, "Marketingowiec", 7000)
    pracownik3 = Pracownik("Mariusz", "Iksiński", 27, "Programista", 9000)
    manager = Manager("Ewa", "Wiśniewska", 40, "Kierownik", 10000)

    print(pracownik1.przedstaw_sie())
    print(pracownik1.info_o_pracy())

    manager.dodaj_do_zespolu(pracownik1)
    manager.dodaj_do_zespolu(pracownik2)
    manager.dodaj_do_zespolu(pracownik3)
    print(manager.przedstaw_sie())
