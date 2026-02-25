palavra_secreta = "amor"
tentativas = 0
letras_acertadas = ''


while True:
    
    tentativas_usuario = input("Digite uma letra: ").lower()
    tentativas += 1


    if len(tentativas_usuario) > 1:
        print('Digite apenas uma letra')
        continue
        
    if tentativas_usuario in palavra_secreta:
        letras_acertadas += tentativas_usuario


    palavra_formada = ''
    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCE GANHOU!')
        print(tentativas)
        letras_acertadas = ''
        tentativas = 0



    


    





