# Remova todos os caracteres duplicados do string abaixo:

def remover_caracteres_duplicados(string):
    caracteres_unicos = []
    for char in string:
        if char not in caracteres_unicos:
            caracteres_unicos.append(char)
    string_sem_duplicados = ''.join(caracteres_unicos)
    return string_sem_duplicados

string_original = input("Digite uma string: ")
string_sem_duplicados = remover_caracteres_duplicados(string_original)
print("String sem caracteres duplicados:", string_sem_duplicados)
