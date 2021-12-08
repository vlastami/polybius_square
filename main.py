from encryption import encryption
from decryption import decryption

print("Polybiova šifra")
run = True

while(run):
    print(f"Vyber akci:")
    print(f"1 - Zašifrování slova")
    print(f"2 - Dešifrování slova")
    print(f"3 - Konec programu")

    wish = int(input("Tvá volba (číslo): "))

    match wish:
        case 1:
            word = input("Zadej slovo k zašifrování: ")
            print(f"Zašifrované slovo: {encryption(word)}")
        case 2:
            option = input("Chceš dešifrovat předchozí slovo? ano/ne")
            if option == ("ano" or "a"):
                cipher = encryption(word)
            else:
                cipher = input("Zadej zašifrované slovo k dešifrování: ")
            print(f"Dešifrované slovo: {decryption(cipher)}")
        case 3:
            run = False

print("Na shledanou!")
