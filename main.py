from cryptography.fernet import Fernet
import os


def main():

    # jesli nie istnieje klucz do szyfrowania to nalezy go utworzyc
    is_exist_encryption_key = os.path.isfile('filekey.key')

    if not is_exist_encryption_key:
        generate_encryption_key()

    # pobranie nazwy pliku
    file_name = input("Podaj nazwe pliku \n")

    # sprawdz istnienie podanego przez uzytkownika pliku
    is_exist_file_name = os.path.isfile(file_name)

    # jesli nie istnieje to zakoncz dzialanie
    if not is_exist_file_name:
        print("Plik nie istnieje")
        return

    # rodzaj akcji szyfrowanie / deszyfrowanie
    action = get_action(file_name)

    # przejscie do odpowiedniej funkcji po wybraniu akcji
    if action:
        decryption_file(file_name)
    else:
        encryption_file(file_name)

    # wiadomosc koncowa
    print("Plik {} jest gotowy".format(file_name))


def generate_encryption_key():

    # wygenerowany klucz
    key = Fernet.generate_key()

    # tworzenie pliku dla wygenerowanego klucza
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)


# pobiera informacje od uzytkownika odpowiednia o zamierzonej akcji
# szyfrowania lub deszyfrowania
def get_action(file_name):
    action = 0
    action_str = "Co chcesz zrobic z plikiem {}? \n" \
                 "0 - szyfrowanie \n" \
                 "1 - deszyfrowanie \n".format(file_name)

    # petla trwa dopoki uzytkownik nie poda 0 lub 1
    while True:
        try:
            action = int(input(action_str))
        except ValueError:
            print("Podaj liczbe 0 lub 1")
            continue
        if action < 0 or action > 1:
            print("Podaj liczbe 0 lub 1")
            continue
        else:
            break

    return action


# metoda szyfrujaca plik
def encryption_file(file_name):

    # sprawdzenie czy istnieje plik z kluczem, a nastepnie otwarcie go
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # uzycie wygenerowanego klucza za pomoca modulu
    fernet = Fernet(key)

    # pobranie i odczytanie podanego pliku przez uzytkownika
    with open(file_name, 'rb') as file:
        original = file.read()

    # szyfrowanie pliku za pomoca modulu fernet
    encrypted = fernet.encrypt(original)

    # ponowne otwarcie pliku podanego przez uzytkownika i zapisanie w nim
    # zaszyfrowanej juz tresci
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# deszyfrowanie podanego pliku
def decryption_file(file_name):

    # sprawdzenie czy istnieje plik z kluczem, a nastepnie otwarcie go
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # uzycie wygenerowanego klucza za pomoca modulu
    fernet = Fernet(key)

    # pobranie i odczytanie zaszyfrowanego pliku przez uzytkownika
    with open(file_name, 'rb') as enc_file:
        encrypted = enc_file.read()

    # deszyfrowanie pliku za pomoca modulu
    decrypted = fernet.decrypt(encrypted)

    # otwarcie pliku i zapisanie w nim odszyfrowanej tresci
    with open(file_name, 'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == '__main__':
    main()
