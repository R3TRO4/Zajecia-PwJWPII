from geompy import *

print("=== Figury 2D ===")
print("Kwadrat: pole =", pole_kwadratu(4), ", obwód =", obwod_kwadratu(4))
print("Prostokąt: pole =", pole_prostokata(3, 7), ", obwód =", obwod_prostokata(3, 7))
print("Koło: pole =", round(pole_kola(6), 4), ", obwód =", round(obwod_kola(6), 4))

print("\n=== Figury 3D ===")
print("Sześcian: objętość =", objetosc_szescianu(3), ", pole =", pole_szescianu(3))
print("Prostopadłościan: objętość =", objetosc_prostopadloscianu(2, 3, 4), ", pole =", pole_prostopadloscianu(2, 3, 4))
print("Kula: objętość =", round(objetosc_kuli(2), 2), ", pole =", round(pole_kuli(2), 2))
