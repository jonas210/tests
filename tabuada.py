def tabuada(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    return

numero_u = input('insira o numero que voce quer ver a tabuada: ')

int_numero = int(numero_u)

tabuada(int_numero)