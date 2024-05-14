import math

def sześcian():
    a = int(input("Podaj długość boku sześcianu: "))
    return a ** 3

def prostopadłościan():
    a = int(input("Podaj długość pierwszej krawędzi podstawy prostopadłościanu: "))
    b = int(input("Podaj długość drugiej krawędzi podstawy prostopadłościanu: "))
    h = int(input("Podaj wysokość prostopadłościanu: "))
    return a*b*h

def kula():
    r = int(input("Podaj długośc promienia kuli: "))
    return (3/4) * math.pi * (r ** 3)