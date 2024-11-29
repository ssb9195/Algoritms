# Bibliotēku importēšana
import string
import random

# Šifrēšanas klase
class MessageEncryptor:
    def __init__(self, key_length=16):
        self.key_length = key_length
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + ' '
        self.key = self.generate_key()

    # Izlases atslēgu ģenerēšana
    def generate_key(self):
        return ''.join(random.choice(self.alphabet) for _ in range(self.key_length))

    # Ziņojumu šifrēšanas funkcija
    def encrypt(self, message):
        encrypted_message = ''
        for i, char in enumerate(message):
            if char in self.alphabet:
                shift = self.alphabet.index(self.key[i % len(self.key)])
                new_index = (self.alphabet.index(char) + shift) % len(self.alphabet)
                encrypted_message += self.alphabet[new_index]
            else:
                encrypted_message += char
        return encrypted_message

    # Funkcija ziņojumu atšifrēšanai
    def decrypt(self, encrypted_message):
        decrypted_message = ''
        for i, char in enumerate(encrypted_message):
            if char in self.alphabet:
                shift = self.alphabet.index(self.key[i % len(self.key)])
                new_index = (self.alphabet.index(char) - shift) % len(self.alphabet)
                decrypted_message += self.alphabet[new_index]
            else:
                decrypted_message += char
        return decrypted_message

    # Atslēgas saglabāšana failā
    def save_key(self, filename):
        with open(filename, 'w') as file:
            file.write(self.key)

    # Atslēgas ielāde no faila
    def load_key(self, filename):
        with open(filename, 'r') as file:
            self.key = file.read().strip()

    # Funkcija, lai parādītu pašreizējo atslēgu
    def show_key(self):
        print(f"Pašreizējā atslēga: {self.key}")

# Darbības izvēlne
def main():
    print("Sveiki!")
    encryptor = MessageEncryptor()

    while True:
        print("\nIzvēle:")
        print("1. Šifrēt ziņojumu")
        print("2. Atšifrēt ziņojumu")
        print("3. Rādīt pašreizējo atslēgu")
        print("4. Saglabāt atslēgu failā")
        print("5. Ielādēt atslēgu no faila")
        print("6. Izēja")

        choice = input("Izvēle darbību: ")

        if choice == '1':
            message = input("Uzrakstiet ziņojumu, lai šifrēt: ")
            encrypted_message = encryptor.encrypt(message)
            print(f"Šifrēts ziņojums: {encrypted_message}")
        elif choice == '2':
            encrypted_message = input("Uzrakstiet ziņojumu, lai atšifrēt: ")
            decrypted_message = encryptor.decrypt(encrypted_message)
            print(f"Atšifrēts ziņojums: {decrypted_message}")
        elif choice == '3':
            encryptor.show_key()
        elif choice == '4':
            filename = input("Ievadiet faila nosaukumu, lai saglabātu atslēgu: ")
            encryptor.save_key(filename)
            print("Atslēga veiksmīgi saglabāta!")
        elif choice == '5':
            filename = input("Ievadiet faila nosaukumu, lai ielādētu atslēgu: ")
            try:
                encryptor.load_key(filename)
                print("Atslēga ir veiksmīgi ielādēta!")
            except FileNotFoundError:
                print("Fails nav atrasts. Lūdzu, mēģiniet vēlreiz.")
        elif choice == '6':
            print("Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")

# Programmas palaišana
if __name__ == "__main__":
    main()
