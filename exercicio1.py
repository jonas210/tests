import time



print("Minha primeira calculadora")
print("Digite 'q' para sair")
print('-' * 30)

while True:
    first_number = input("Digite seu primeiro numero: ")

    if first_number.lower() == 'q':
       print('Tchau :)')
       time.sleep(1.5)
       break


    try:
        int_first = int(first_number)
    except ValueError:
       print("Digite apenas números!")
       time.sleep(0.7)
       continue


    second_number = input("Digite seu segundo numero: ")
    if second_number.lower() == 'q':
       print('Tchau :)')
       time.sleep(1.5)
       break


    try:
        int_second = int(second_number)
    except ValueError:
        print("Digite apenas números!")
        time.sleep(0.7)
        continue


    operator = input("Digite o operador (+, -, * ou /): ")

    if operator.lower() == 'q':
       print('Tchau :)')
       time.sleep(1.5)
       break



    if operator == '+':
       resultado = int_first + int_second

    elif operator == '-':
      resultado = int_first - int_second
    
    elif operator == '*':
       resultado = int_first * int_second

    elif operator == '/':
       try:
         resultado = int_first / int_second
       except ZeroDivisionError:
         print("Divisão com zero não permitida!")
         time.sleep(0.7)
         continue

    else:
        print("Operador invalido.")
        time.sleep(0.7)
        continue

    print(f'O resultado é: {resultado}')

    sair = input("Quer continuar? [sim]/[não] ").lower().strip().startswith("n")
    if sair:
       print("Tchau :)")
       time.sleep(1.5)
       break






