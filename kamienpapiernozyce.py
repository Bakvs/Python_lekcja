import random
def wyborgracza():
    gracz = input("Wybierz kamień, papier lub nożyce: ")
    while gracz not in ["kamień", "papier", "nożyce"]:
        print("Niepoprawny wybór, spróbuj ponownie.")
        gracz = input("Wybierz kamień, papier lub nożyce: ")
    return gracz

def wyborkomputera():
    return random.choice(["kamień", "papier", "nożyce"])

def gra(gracz, komputer):
    if gracz == komputer:
        return "REMIS"
    elif (gracz == "papier" and komputer == "kamień") or \
          (gracz == "kamień" and komputer == "nożyce") or \
          (gracz == "nożyce" and komputer == "papier"):
        return "WYGRANA"
    else:
        return "PRZEGRANA"
    
def main():
    print("Witaj w grze kamień, papier lub nożyce")
    while True:
        gracz = wyborgracza()
        komputer = wyborkomputera()
        print("Twój wybór: " + gracz)
        print("Wybor komputera: " + komputer)
        print(gra(gracz, komputer))
        play_again = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
        if play_again == "tak":
            return main()
        else:
            print("Dziękujemy za grę")
            break
if __name__ == "__main__":
    main()