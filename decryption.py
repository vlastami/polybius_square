import alphabet as a


def decryption(cipher):
    list_of_letters = cipher.split()
    new_word = ""
    for item in range(len(list_of_letters)):
        new_word += get_key(list_of_letters[item])
    return new_word


def get_key(val):
    for key, value in a.alphabet.items():
        if val == value:
            return key
    raise KeyError
