import random

def gracz():
    gracz = input("Wybierz kamień, papier lub nożyce").lower()
    while gracz not in ['kamień', 'papier', 'nożyce']:
        print("Niepoprawny wybór, spróbuj ponownie.")
        gracz = input("Wybierz kamień, papier lub nożyce").lower()
    return gracz

def komputer():
    return random(['kamień', 'papier', 'nożyce'])

def gra(gracz, komputer):
    if gracz == komputer:
        return "REMIS"
    elif (gracz == 'papier' and komputer == 'kamień') or \
         (gracz == 'kamień' and komputer == 'nożyce') or \
         (gracz == 'nożyce' and komputer == 'papier'):
        return "WYGRANA"
    else:
        return "PRZEGRANA"
    
def main():
    print("Witaj w grze kamień, papier lub nożyce")
    while True:
        gracz = gracz()
        komputer = komputer()
        print("Twój wybór: {gracz}")
        print("Wybor komputera: {komputer}")
        print(gra(gracz, komputer))
        play_again = input("Chcesz zagrać jeszcze raz? (tak/nie): ").lower()
        if play_again == 'tak':
            return main
        else:
            print("Dziękujemy za grę!")
            break