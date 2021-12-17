import alphabet as a


def encryption(word):
    new_word = ""
    for letter in word:
        letter = letter.replace("ě", "e"). \
            replace("é", "e"). \
            replace("š", "s"). \
            replace("č", "c"). \
            replace("ř", "r"). \
            replace("ž", "z"). \
            replace("ý", "y"). \
            replace("á", "a"). \
            replace("í", "i"). \
            replace("ů", "u"). \
            replace("ú", "u")

        new_word += a.alphabet[letter] + " "

    return new_word