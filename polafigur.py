import math

def kwadrat():
    a = int(input("Podaj długość boku kwadratu: "))
    return a ** 2

def prostokat():
    a = int(input("Podaj długość podstawy trójkąta: "))
    b = int(input("Podaj długość wysokości trójkąta: "))
    return a * b

def trojkat():
    a = int(input("Podaj długość podstawy trójkąta: "))
    h = int(input("Podaj długość wysokości trójkąta: "))
    return (a * h)/2

def romb():
    e = int(input("Podaj długość pierwszej przekątnej rombu: "))
    f = int(input("Podaj długość drugiej przekątnej rombu: "))
    return e * f

def kolo():
    r = int(input("Podaj długośc promienia koła: "))
    return math.pi * r ** 2

def rownoleglobok():
    a = int(input("Podaj długość podstawy równoległoboku: "))
    h = int(input("Podaj długość wysokości równoległoboku: "))
    return a * h

def trapez():
    a = int(input("Podaj długość pierwszej podstawy trapezu: "))
    b = int(input("Podaj długość drugiej podstawy trapezu: "))
    h = int(input("Podaj długość wysokości trapezu: "))
    return ((a + b) * h)/2

print("1. kwadrat")
print("2. prostokąt")
print("3. trójkąt")
print("4. romb")
print("5. koło")
print("6. równoległobok")
print("7. trapez")

wybor = int(input("Wybierz figurę, której pole chcerz obliczyć (1-7): "))

if wybor == 1:
    print("Pole kwadratu wynosi: ", kwadrat())
elif wybor == 2:
    print("Pole prostokąta wynosi: ", prostokat())
elif wybor == 3:
    print("Pole trójkąta wynosi: ", trojkat())
elif wybor == 4:
    print("Pole rombu wynosi: ", romb())
elif wybor == 5:
    print("Pole koła wynosi: ", kolo())
elif wybor == 6:
    print("Pole równoległoboku wynosi: ", rownoleglobok())
elif wybor == 7:
    print("Pole trapezu wynosi: ", trapez())
else:
    print("Niepoprawny wybór")