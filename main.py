from encryption import encryption

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
            print("to be implemented")
        case 3:
            run = False

print("Na shledanou!")
