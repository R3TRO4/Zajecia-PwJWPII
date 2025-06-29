from typing import Generator

"""
Zaimplementuj funkcję wykorzystującą generator do zwracania kolejnych liczb ciągu
Fibonacciego. Generator powinien umożliwiać iteracyjne pobieranie wartości bez
konieczności przechowywania całej sekwencji w pamięci.
"""

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(50):
    print(next(gen))
