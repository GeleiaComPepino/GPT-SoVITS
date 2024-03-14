import epitran
ipa_alphabet = {"": 0, "<pad>": 1, "</s>": 2, "<unk>": 3, "|": 4, "A": 5, "E": 6, "O": 7, "S": 8, "R": 9, "I": 10, "N": 11, "D": 12, "M": 13, "T": 14, "U": 15, "C": 16, "L": 17, "P": 18, "V": 19, "G": 20, "F": 21, "H": 22, "Q": 23, "B": 24, "Ã": 25, "Ç": 26, "É": 27, "Á": 28, "Z": 29, "J": 30, "X": 31, "Í": 32, "Ó": 33, "Ê": 34, "-": 35, "Õ": 36, "À": 37, "Ú": 38, "Ô": 39, "Â": 40, "Y": 41, "K": 42, "W": 43}
def invert_dict(d):
    return {v: k for k, v in d.items()}

def text_normalize(text):
    # todo: eng text normalize
    return text.replace(";", ",")
def g2p(word):
    inverted_dict = invert_dict(ipa_alphabet)
    word = word.lower()
    epi = epitran.Epitran('por-Latn')  # Portuguese Latin script
    ipa_transcription = epi.transliterate(word)
    ipa_transcription = [char for char in ipa_transcription if char != ' ' and char != '.' and char != '̃' and char != ',' and char != '?']
    return ipa_transcription
if __name__ == "__main__":
    print(g2p("aáàâãbcçdeéêfghiíjklmnoóôõpqrstuúüvwxyz"))