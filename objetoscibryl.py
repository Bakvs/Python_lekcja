import math

def szescian():
    a = int(input("Podaj długość boku sześcianu: "))
    return a ** 3

def prostopadloscian():
    a = int(input("Podaj długość pierwszej krawędzi podstawy prostopadłościanu: "))
    b = int(input("Podaj długość drugiej krawędzi podstawy prostopadłościanu: "))
    H = int(input("Podaj wysokość prostopadłościanu: "))
    return a * b * H

def kula():
    r = int(input("Podaj długośc promienia kuli: "))
    return (3/4) * math.pi * (r ** 3)

def walec():
    r = int(input("Podaj długośc promienia podstawy: "))
    H = int(input("Podaj wysokość walca: "))
    return math.pi * (r ** 2) * H

print("1. sześcian")
print("2. prostopadłościan")
print("3. kula")
print("4. walec")

wybor = int(input("Wybierz bryłę, której objętość chcerz obliczyć (1-4): "))

if wybor == 1:
    print("Pole sześcianu wynosi: ", szescian())
elif wybor == 2:
    print("Pole prostopadłościanu wynosi: ", prostopadloscian())
elif wybor == 3:
    print("Pole kuli wynosi: ", kula())
elif wybor == 4:
    print("Pole walca wynosi: ", walec())