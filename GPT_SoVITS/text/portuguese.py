import os
import re

def text_normalize(text):
    return text.replace(";", ",")

def load_phonetic_dict(file_path):
    phonetic_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, phonemes = re.split(r'\s+', line.strip(), 1)
            phonetic_dict[word] = phonemes.split()
    return phonetic_dict

def g2p(text):
    textResult = []
    for word in text.split():
        current_file_path = os.path.dirname(__file__)
        file_path = os.path.join(current_file_path, 'br-pt.txt')
        phonetic_dict = load_phonetic_dict(file_path)
        phonetic_representation = phonetic_dict.get(word, [])
        for letter in phonetic_representation:
            textResult.append(letter)
    return textResult
if __name__ == "__main__":
    print(g2p('teste infantaria'))
