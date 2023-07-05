# Verifique se a string é um anagrama de um palindromo:

def is_anagram_palindrome(string):
    char_counts = {}
    odd_count = 0

    # Contagem de ocorrências de cada caractere na string
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Verificação de quantos caracteres têm uma contagem ímpar
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1

    # Se tiver mais de um caractere com contagem ímpar, não é palíndromo
    if odd_count > 1:
        return False, None

    # Construção do palíndromo a partir dos caracteres com contagem ímpar
    palindrome = ""
    odd_char = ""
    for char, count in char_counts.items():
        if count % 2 != 0:
            odd_char = char
        palindrome += char * (count // 2)

    palindrome += odd_char + palindrome[::-1]

    return True, palindrome


string = input("Digite uma string: ")
is_palindrome, palindrome = is_anagram_palindrome(string)
print("É um anagrama de um palíndromo:", is_palindrome)
if is_palindrome:
    print("Palíndromo encontrado:", palindrome)
