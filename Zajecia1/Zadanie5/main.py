
"""
Zaprojektuj system dla inteligentnego telefonu, który posiada funkcje komunikacji i
rozrywki. Zadanie wymaga przemyślenia, czy lepiej zastosować wielodziedziczenie czy
kompozycję.
Scenariusz:
• Każdy inteligentny telefon ma podstawowe cechy, takie jak model i producent.
• Funkcjonalność komunikacji obejmuje wysyłanie wiadomości.
• Funkcjonalność rozrywki obejmuje odtwarzanie muzyki.
• Istnieje telefon, który ma obie te funkcje.
Wymagania:
1. Utwórz klasę Telefon z atrybutami model i producent.
2. Utwórz osobne klasy:
a. Komunikacja z metodą wyslij_wiadomosc(odbiorca, tresc)
b. Rozrywka z metodą odtworz_muzyke(utwor)
3. Zastanów się, czy stworzyć klasę Smartphone dziedziczącą jednocześnie po
Telefon, Komunikacja i Rozrywka (wielodziedziczenie) lub zastosować
kompozycję, czyli w klasie Smartphone umieścić atrybuty będące obiektami
klas Komunikacja i Rozrywka.
4. Test:
a. Jeśli zdecydujesz się na wielodziedziczenie – zaimplementuj klasę
Smartphone i przetestuj jej funkcjonalności.
b. Jeśli wybierzesz kompozycję – stwórz obiekty funkcjonalności i przypisz je
do telefonu, a następnie wywołaj odpowiednie metody.
"""

# Klasa bazowa Telefon
class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

# Funkcjonalność komunikacji
class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        print(f"Wysyłanie wiadomości do {odbiorca}: {tresc}")

# Funkcjonalność rozrywki
class Rozrywka:
    def odtworz_muzyke(self, utwor):
        print(f"Odtwarzanie utworu: {utwor}")

# Smartfon korzystający z kompozycji
class Smartphone:
    def __init__(self, model, producent):
        self.telefon = Telefon(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()

    def wyslij_wiadomosc(self, odbiorca, tresc):
        self.komunikacja.wyslij_wiadomosc(odbiorca, tresc)

    def odtworz_muzyke(self, utwor):
        self.rozrywka.odtworz_muzyke(utwor)

    def info(self):
        print(f"Smartphone: {self.telefon.model} ({self.telefon.producent})")

if __name__ == "__main__":
    moj_telefon = Smartphone("Galaxy S23", "Samsung")
    moj_telefon.info()
    moj_telefon.wyslij_wiadomosc("Alicja", "Cześć, co słychać?")
    moj_telefon.odtworz_muzyke("Imagine Dragons - Believer")
