arpa_to_portuguese = {
    "AH0": "a",   # similar to the 'a' in "casa" (house)
    "S": "s",     # same as English
    "AH1": "á",   # similar to the 'á' in "água" (water)
    "EY2": "é",   # similar to the 'é' in "pé" (foot)
    "AE2": "é",   # similar to the 'é' in "pé" (foot)
    "EH0": "ê",   # similar to the 'ê' in "vê" (see)
    "OW2": "ô",   # similar to the 'ô' in "só" (alone)
    "UH0": "u",   # similar to the 'u' in "burro" (donkey)
    "NG": "ng",   # same as English
    "B": "b",     # same as English
    "G": "g",     # same as English
    "AY0": "ai",  # similar to the 'ai' in "pai" (father)
    "M": "m",     # same as English
    "AA0": "a",   # similar to the 'a' in "casa" (house)
    "F": "f",     # same as English
    "AO0": "ou",  # similar to the 'ou' in "pouco" (few)
    "ER2": "er",  # similar to the 'er' in "poder" (to be able)
    "UH1": "ú",   # similar to the 'ú' in "útil" (useful)
    "IY1": "i",   # same as English 'i'
    "AH2": "á",   # similar to the 'á' in "água" (water)
    "DH": "d",    # same as English 'd'
    "IY0": "i",   # same as English 'i'
    "EY1": "ei",  # similar to the 'ei' in "feira" (fair)
    "IH0": "í",   # similar to the 'í' in "ímpar" (odd)
    "K": "k",     # same as English
    "N": "n",     # same as English
    "W": "w",     # same as English
    "IY2": "i",   # same as English 'i'
    "T": "t",     # same as English
    "AA1": "á",   # similar to the 'á' in "água" (water)
    "ER1": "er",  # similar to the 'er' in "poder" (to be able)
    "EH2": "ê",   # similar to the 'ê' in "vê" (see)
    "OY0": "oi",  # similar to the 'oi' in "boi" (ox)
    "UH2": "u",   # similar to the 'u' in "burro" (donkey)
    "UW1": "u",   # similar to the 'u' in "mundo" (world)
    "Z": "z",     # same as English
    "AW2": "ou",  # similar to the 'ou' in "pouco" (few)
    "AW1": "ou",  # similar to the 'ou' in "pouco" (few)
    "V": "v",     # same as English
    "UW2": "u",   # similar to the 'u' in "mundo" (world)
    "AA2": "á",   # similar to the 'á' in "água" (water)
    "ER": "er",   # similar to the 'er' in "poder" (to be able)
    "AW0": "ou",  # similar to the 'ou' in "pouco" (few)
    "UW0": "u",   # similar to the 'u' in "mundo" (world)
    "R": "r",     # same as English
    "OW1": "ô",   # similar to the 'ô' in "só" (alone)
    "EH1": "ê",   # similar to the 'ê' in "vê" (see)
    "ZH": "j",    # similar to the 'j' in "já" (already)
    "AE0": "a",   # similar to the 'a' in "casa" (house)
    "IH2": "i",   # same as English 'i'
    "IH": "i",    # same as English 'i'
    "Y": "i",     # same as English 'i'
    "JH": "j",    # same as English 'j'
    "P": "p",     # same as English
    "AY1": "ai",  # similar to the 'ai' in "pai" (father)
    "EY0": "ei",  # similar to the 'ei' in "feira" (fair)
    "OY2": "oi",  # similar to the 'oi' in "boi" (ox)
    "TH": "t",    # similar to the 't' in "táxi" (taxi)
    "HH": "",     # typically silent, like 'h' in Portuguese
    "D": "d",     # same as English
    "ER0": "er",  # similar to the 'er' in "poder" (to be able)
    "CH": "ch",   # same as English
    "AO1": "ou",  # similar to the 'ou' in "pouco" (few)
    "AE1": "a",   # similar to the 'a' in "casa" (house)
    "AO2": "ou",  # similar to the 'ou' in "pouco" (few)
    "OY1": "oi",  # similar to the 'oi' in "boi" (ox)
    "AY2": "ai",  # similar to the 'ai' in "pai" (father)
    "IH1": "i",   # same as English 'i'
    "OW0": "ô",   # similar to the 'ô' in "só" (alone)
    "L": "l",     # same as English
    "SH": "ch",   # similar to the 'ch' in "chave" (key)
    "K": "c"
}
def text_normalize(text):
    # todo: eng text normalize
    return text.replace(";", ",")
arpa_to_portuguese_inverted = {value: key for key, value in arpa_to_portuguese.items()}
def g2p(word):
    translated_word = []
    for phoneme in word:
        if phoneme.lower() not in [' ', '.', ',']:
            character = arpa_to_portuguese_inverted.get(phoneme.lower(), "")
            if character == '':
                pass
            else:
                translated_word.append(character)
    return translated_word