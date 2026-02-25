import random

def aleatorizar():
    return random.randint(1, 100)

def user_continuar():
    continuar = input("Voce quer continuar? [sim]/[não] ").lower().startswith('s')
    return continuar


print("Jogo da adivinhação!")
while True:
    numero_aleatorio = aleatorizar()
    tentativas = 0

    while True:
        try:
            tentativa_usuario = int(input('Qual o numero que voce acha que é? '))
        except ValueError:
            print("Digite apenas numeros!")
            continue

        tentativas += 1

        if tentativa_usuario == numero_aleatorio:
            letra_tentativa = "tentativas" if tentativas > 1 else "tentativa"
            print(f'Você acertou em {tentativas} {letra_tentativa}!')  
            break
        elif tentativa_usuario > numero_aleatorio:
            print('Seu numero é MAIOR que o numero secreto')
        else:
            print('Seu numero é MENOR que o numero secreto')

    if not user_continuar():
        print("obrigado por jogar")
        break




