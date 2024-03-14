import epitran
ipa_alphabet = {
    'a': 'æ', 'b': 'b', 'c': 'k', 'd': 'd', 'e': 'ɛ', 'f': 'f',
    'g': 'ɡ', 'h': 'h', 'i': 'ɪ', 'j': 'dʒ', 'k': 'k', 'l': 'l',
    'm': 'm', 'n': 'n', 'o': 'oʊ', 'p': 'p', 'q': 'kw', 'r': 'ɹ',
    's': 's', 't': 't', 'u': 'ʊ', 'v': 'v', 'w': 'w', 'x': 'ks',
    'y': 'j', 'z': 'z'
}

def text_normalize(text):
    # todo: eng text normalize
    return text.replace(";", ",")
def g2p(word):
    word = word.lower()
    epi = epitran.Epitran('por-Latn')  # Portuguese Latin script
    ipa_transcription = epi.transliterate(word)
    # Remove spaces from the IPA transcription
    ipa_transcription = [char for char in ipa_transcription if char != ' ' and char != '.' and char != '̃' and char != ',' and char != '?']
    return ipa_transcription
if __name__ == "__main__":
    print(g2p("aáàâãbcçdeéêfghiíjklmnoóôõpqrstuúüvwxyz"))