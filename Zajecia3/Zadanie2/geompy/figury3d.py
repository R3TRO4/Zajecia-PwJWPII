import math

def objetosc_szescianu(bok):
    return bok ** 3

def pole_szescianu(bok):
    return 6 * bok ** 2

def objetosc_prostopadloscianu(a, b, h):
    return a * b * h

def pole_prostopadloscianu(a, b, h):
    return 2 * (a * b + a * h + b * h)

def objetosc_kuli(promien):
    return (4 / 3) * math.pi * promien ** 3

def pole_kuli(promien):
    return 4 * math.pi * promien ** 2
