# Encontre a substring mais longa na string abaixo:

def is_palindromo(string):
    reversed_string = string[::-1]
    return string == reversed_string

def encontrar_palindromo_mais_longo(string):
    palindromo_mais_longo = ''

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if is_palindromo(substr) and len(substr) > len(palindromo_mais_longo):
                palindromo_mais_longo = substr

    return palindromo_mais_longo

string = input("Digite uma string: ")
palindromo_mais_longo = encontrar_palindromo_mais_longo(string)
print("Palíndromo mais longo encontrado:", palindromo_mais_longo)
