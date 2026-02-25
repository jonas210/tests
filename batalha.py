import random
import time

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self._nome = nome
        self._vida = vida
        self._ataque = ataque
        self._defesa = defesa

    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        outro.receber_dano(dano)

    def receber_dano(self, valor):
        self._vida -= valor
        if self._vida < 0:
            self._vida = 0
        print(f"Agora, {self._nome} tem {self._vida} pontos de vida")


    def esta_vivo(self):
        return self._vida > 0

    def __str__(self):
        return f'{self._nome} - Vida: {self._vida}, Ataque: {self._ataque}, Defesa: {self._defesa}'
        

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=20, defesa=10)

    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        outro.receber_dano(dano)

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=25, defesa=5)


    def atacar(self, outro):
        dano = self._ataque - outro._defesa
        if dano < 0:
            dano = 0
        dano = random.randint(int(dano*0.8), int(dano*1.2))
        print(f'{self._nome} ataca {outro._nome} e causa {dano} de dano!')
        outro.receber_dano(dano)


def batalhar(personagem1, personagem2):
    print(personagem1)
    print(personagem2)
    print()

    while personagem1.esta_vivo() and personagem2.esta_vivo():
        personagem1.atacar(personagem2)
        time.sleep(2)
        if not personagem2.esta_vivo():
            print(f'\n {personagem2._nome} foi derrotado! {personagem1._nome} foi o vencedor.')
            break
        personagem2.atacar(personagem1)
        time.sleep(2)
        if not personagem1.esta_vivo():
            print(f'\n {personagem1._nome} foi derrotado! {personagem2._nome} foi o vencedor.')
            break
        print()

guerreiro = Guerreiro("Jonas")
mago = Mago("Sponge")

batalhar(guerreiro, mago)

