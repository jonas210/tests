import os

lista = []

def inserir():
    os.system('cls')
    valor = input("Valor: ")
    lista.append(valor)

def apagar():
    os.system('cls')
    if not lista:
        print("Nada para apagar")
        return
    
    indice = input("Escolha o indice para excluir: ")

    if not indice.isdigit():
        print("Digite apenas números.")
        return
    
    int_indice = int(indice)

    if int_indice < 0 or int_indice >= len(lista):
        print("Índice inválido.")
        return

    del lista[int_indice]
    print("Item apagado com sucesso!")
    
def listar():
    os.system('cls')

    if not lista:
        print("Nada para listar")
        return
    
    for indice, itens in enumerate(lista):
        print(indice, itens)

while True:
    print("Lista de compras!")
    print("-" * 30)
    print("Selecione uma opção:")
    
    entrada = input("[i]nserir, [a]pagar, [l]istar, [s]air \n>").lower()
    if entrada == 's':
        print("Saindo do programa")
        break

    opcoes = {
        "i": inserir,
        "a": apagar,
        "l": listar
    }

    try:
        opcoes[entrada]()
    except KeyError:
        print(f"Opção invalida, tente novamente")
        continue
