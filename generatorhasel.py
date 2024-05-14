import random
import string

def generator(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Podaj długość hasła: "))
    if length <= 0:
        print("Długość hasła musi być większa od zera.")
        return
    password = generator(length)
    print("Wygenerowane hasło:" + password)

if __name__ == "__main__":
    main()