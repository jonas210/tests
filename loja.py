
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Produto:
    def __init__(self, nome, qtd):
        if qtd < 0:
            raise ValueError("O valor inicial nao pode ser negativo")
        
        self.nome = nome
        self.qtd = qtd

    def entrada(self, qtd):
        if qtd <= 0:
            raise ValueError("Quantidade de entrada invalida")
        
        self.qtd += qtd

    def saida(self, qtd):
        if qtd <= 0:
            raise ValueError("Quantidade de saida invalida")
        
        if qtd > self.qtd:
            raise ValueError("Estoque insuficiente")
        
        self.qtd -= qtd

    def __str__(self):
        return f'O produto {self.nome}: tem {self.qtd} unidade(s)'

class Vendas:
    def __init__(self, cliente, produto, qtd):
        self.cliente = cliente
        self.produto = produto
        self.qtd = qtd

    def realizar(self):
        self.produto.saida(self.qtd)
        return (
            f'Venda realizada com sucesso!\n'
            f'Cliente: {self.cliente.nome}\n'
            f'Produto: {self.produto.nome}\n'
            f'Quantidade: {self.qtd}'
        )
    
clientes = {}
produtos = {}


def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")

    if cpf in clientes:
        print("CPF já cadastrado!")
        return
    
    clientes[cpf] = Cliente(nome, cpf)
    print("Cliente cadastrado com sucesso")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    try:
        qtd = int(input("Quantidade inicial: "))
    except ValueError:
        print("Digite um numero valido")
        return

    if nome in produtos:
        resp = input("Produto ja existe. Deseja adicionar as unidades digitadas?: ").lower()
        if resp.startswith("s"):
            produtos[nome].entrada(qtd)
            print("Unidade(s) adicionadas")

        return
        
    produtos[nome] = Produto(nome, qtd)
    print("Produto cadastrado com sucesso")

def realizar_venda():
    cpf = input("CPF do cliente: ")
    nome_produto = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))

    if cpf not in clientes:
        print("Cliente não encontrado!")
        return
    
    if nome_produto not in produtos:
        print("Produto não encontrado!")
        return
    
    venda = Vendas(clientes[cpf], produtos[nome_produto], qtd)

    try:
        print(venda.realizar())
        print(produtos[nome_produto])
    except ValueError as e:
        print(f'Erro: {e}')


while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Cadastrar produto")
    print("3 - Realizar venda")
    print("4 - Listar produtos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        cadastrar_produto()
    
    elif opcao == "3":
        realizar_venda()

    elif opcao == "4":
        for produto in produtos.values():
            print(produto)
    
    elif opcao == "0":
        break

    else:
        print("Opção invalida.")
    




