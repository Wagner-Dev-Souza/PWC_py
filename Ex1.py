# Reverta a ordem das palavras nas frases mantendo a ordem das palavras:

def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    frase_invertida = ' '.join(palavras_invertidas)
    return frase_invertida

frase_original = input("Digite uma frase: ")
frase_invertida = inverter_ordem_palavras(frase_original)
print("Frase invertida:", frase_invertida)