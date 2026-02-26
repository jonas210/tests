import os

lista = []

def inserir():
    os.system('cls')
    valor = input("Valor: ")
    lista.append(valor)

def apagar():
    os.system('cls')
    if not len(lista):
        print("Nada para apagar")
        return
    
    indice = input("Escolha o indice para excluir: ")
    try:
        int_indice = int(indice)
        del lista[int_indice]
    except:
        print("Não foi possivel excluir esse indice")
    
def listar():
    os.system('cls')

    if not len(lista):
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
    except Exception as e:
        print(f"Erro: {e}")
        continue
