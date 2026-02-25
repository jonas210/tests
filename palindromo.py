import re

def palindromo(texto):
    nome_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto)

    nome_limpo = nome_limpo.lower()

    return nome_limpo == nome_limpo[::-1]



while True:
    entrada = input("O que você quer verificar?")

    if entrada.lower() == 'q':
        break

    if palindromo(entrada):
        print("É palindromo!")
    
    else:
        print("Não é palindromo")

