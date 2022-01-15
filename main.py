from cryptography.fernet import Fernet


def main():
    file_name = input("Podaj nazwe pliku \n")

    action = get_action(file_name)

    if action:
        decryption_file(file_name)
    else:
        encryption_file(file_name)

    print("Plik {} jest gotowy".format(file_name))


def get_action(file_name):
    action = 0
    action_str = "Co chcesz zrobic z plikiem {}? \n" \
                 "0 - szyfrowanie \n" \
                 "1 - deszyfrowanie \n".format(file_name)

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


def encryption_file(file_name):

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(file_name, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decryption_file(file_name):

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open(file_name, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open(file_name, 'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == '__main__':
    main()
