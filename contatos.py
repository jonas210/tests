"""
Docstring for contatos
"""

class Contato:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    def corresponde(self, valor):
        return valor in self._nome or valor == self._telefone

    def __str__(self):
        return f'{self._nome}: {self._telefone}'

class Agenda:
    def __init__(self):
        self._contatos = {}

    def adicionar_contato(self):
        contato_nome = input("Digite o nome: ")

        while True:
            contato_tel = input("Digite o numero: ")
            if len(contato_tel) == 11 and contato_tel.isdigit():
                break
            print("Numero invalido")


        if contato_nome in self._contatos or any(
            contato_tel == contato._telefone
            for contato in self._contatos.values()
        ):
            print("Contato já existe")

        else:
            self._contatos[contato_nome] = Contato(contato_nome, contato_tel)
            print("Contato adicionado com sucesso")

    def excluir_contato(self):
        if not self._contatos:
            print("Nenhum contato para excluir. \n")
            return
        
        buscar_contato = input("Digite o nome ou numero do contato que deseja excluir: ")

        for nome, contato in list(self._contatos.items()):
            if contato.corresponde(buscar_contato):
                del self._contatos[nome]
                print("Contato excluido com sucesso")
                return

        print("Contato não existe")

    def listar_contato(self):
        if not self._contatos:
            print(f"Nenhum contato cadastrado. \n")
            return
        
        for contato in self._contatos.values():
            print(contato)


agenda = Agenda()

while True:
    print()
    print("Agenda de contatos!")
    print('-' * 20)
    print('Adicionar contato (1)')
    print('Excluir contato (2)')
    print('Listar contatos (3)')
    print('Sair do programa (4)')
    escolha = input(f"Digite o uma das opções acima: \n")

    if escolha == '4':
        print("Obrigado por usar meu programa! :)")
        break

    opcoes = {
        '1': agenda.adicionar_contato,
        '2': agenda.excluir_contato,
        '3': agenda.listar_contato
    }
    try:
        opcoes[escolha]()
    except KeyError:
        print("Opção invalida, tente de novo")
        continue


