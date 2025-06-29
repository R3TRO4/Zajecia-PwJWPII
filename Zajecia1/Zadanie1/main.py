import json

class ModelAI:

    # Atrybut klasowy
    liczba_modeli = 0

    # Konstruktor inicjalizujący atrybuty instancji
    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu # Inicjalizacja nazwy
        self.wersja = wersja # Inicjalizacja wersji
        ModelAI.liczba_modeli += 1 # inkrementacja licznika modeli przy utworzeniu każdego modelu

    @classmethod
    def nowy_model(cls):
        return cls("DomyślnyModel", 1.0) # Tworzenie nowego obiektu

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli # Zwracanie liczby utworzonych modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        # Otwarcie pliku o nazwie pod zmienną "nazwa_pliku". Atrybut "r" od "read". as file nadanie aliasu plikowi
        with open(nazwa_pliku, "r") as file:
            data = json.load(file) # pobranie danych z pliku "file" do zmiennej "data"
            nazwa_modelu = data.get("name") # przypisanie do nazwy modelu wartości spod atrybutu "name"
            wersja = data.get("version") # przypisanie do wersji modelu wartości spod atrybutu "version"
            model4 = ModelAI(nazwa_modelu, wersja) # utworzenie modelu z nazwy modelu i wersji wziętych z pliku
            return model4 # zwrócenie utworzonego modelu

if __name__ == '__main__':

    # Tworzenie modeli
    model1 = ModelAI("GPT-4", 4.0) # GPT-4
    model2 = ModelAI("GPT-3.5", 3.5) # GPT-3.5
    model3 = ModelAI.nowy_model() # Domyślny model
    model4 = ModelAI.z_pliku("model.json") # Model z pliku

    print(model1.nazwa_modelu, model1.wersja) # GPT-4
    print(model2.nazwa_modelu, model2.wersja) # GPT-3.5
    print(model3.nazwa_modelu, model3.wersja) # Domyslny model
    print(model4.nazwa_modelu, model4.wersja) # Model z pliku
    print(ModelAI.ile_modeli()) # Ilosc utworzonych modeli