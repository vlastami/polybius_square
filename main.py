from encryption import encryption
from decryption import decryption

print("Polybiova šifra")
run = True

while(run):
    print(f"Vyber akci:")
    print(f"1 - Zašifrování slova")
    print(f"2 - Dešifrování slova")
    print(f"3 - Konec programu")

    try:
        wish = int(input("Tvá volba (číslo): "))

        match wish:
            case 1:
                try:
                    word = input("Zadej slovo k zašifrování: ")
                    print(f"Zašifrované slovo: {encryption(word)}")
                except KeyError:
                    print("Zadávej pouze písmena")

            case 2:
                option = input("Chceš dešifrovat předchozí slovo? ano/ne").lower()
                if option == ("ano" or "a"):
                    cipher = encryption(word)
                else:
                    try:
                        cipher = input("Zadej zašifrované slovo k dešifrování: ")
                    except KeyError:
                        print("Zadávej pouze písmena")

                print(f"Dešifrované slovo: {decryption(cipher)}")

            case 3:
                run = False
    except ValueError:
        print("Zkus to znovu, zadej číslo.")

print("Na shledanou!")
