def palindromo(nome):
    nome_limpo = nome.replace(" ", "").lower()

    if not nome_limpo.isalpha():
        print("Digite algo válido.")
        return

    if nome_limpo == nome_limpo[::-1]:
        print(f'{nome_limpo} é palindromo!')
    else:
        print("Não é palindromo")



nome_u = input("O que voce quer verificar? ")

palindromo(nome_u)


