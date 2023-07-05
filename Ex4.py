# Coloque em maiúscula a primeira letra de cada frase na string:

def capitalize_first_letter(string):
    return string[0].upper() + string[1:]

def capitalize_first_letter_of_each_sentence(string):
    sentences = re.split(r'([.?!]\s+)', string)
    capitalized_sentences = [capitalize_first_letter(sentence) for sentence in sentences]
    capitalized_string = ''.join(capitalized_sentences)
    return capitalized_string

import re

string = input("Digite uma string: ")
capitalized_string = capitalize_first_letter_of_each_sentence(string)
print("String com primeira letra de cada frase em maiúsculo:", capitalized_string)
