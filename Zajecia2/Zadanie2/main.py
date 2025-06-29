from typing import List

"""
Zaimplementuj funkcję average, która przyjmuje listę liczb zmiennoprzecinkowych i
zwraca ich średnią. Użyj podpowiedzi typów.
"""

def average(numbers: List[float], precision: int = 2) -> float:
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    avg = sum(numbers) / len(numbers)
    return round(avg, precision)


# Przykładowe dane
przykladowe_liczby = [4.0, 7.5, 3.0, 9.2, 6]

# Obliczenie i wyświetlenie średniej
wynik = average(przykladowe_liczby)
print(f"Średnia z {przykladowe_liczby} to {wynik}")