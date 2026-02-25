def main():
  print("calculadora!")
  print("digite q para sair")
  print("-" * 30)
  
def entradaNumeros():
  while True:
    a = input("Insira um numero: ")
    if a.lower() == "q": 
      return "q", "q"
    
    b = input("Insira outro numero: ")
    if b.lower() == "q": 
      return "q", "q"
    
    try:
      return float(a), float(b)
    except ValueError:
      print("Digite apenas numeros")
  
  
def entradaOperador():
  while True:
    operador = input(f"Insira o seu operador \n[+][-][/][*]: ")
    if operador.lower() == "q": 
       return "q"
    if operador in ["+", "-", "*", "/"]:
      return operador
    print("Operador invalido")
  
  
def sair():
  while True:
    entrada = input("Deseja tentar novamente?[sim][nao]: ").strip()
    if entrada.lower() == "sim":
      return True
    elif entrada.lower() == "nao":
      print("Obrigado por usar minha calculadora")
      return False
    else:
      print("Erro, digite novamente")
  
  
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

main()

while True: 
    a, b = entradaNumeros()
    if "q" in [a, b]: 
        break
    op = entradaOperador()
    if op == "q":
        break
    resultado = 0


    operacoes = {
        "+": soma,
        "-": subtracao,
        "*": multiplicacao,
        "/": divisao
    }

    try:
        resultado = operacoes[op](a, b)
    except ZeroDivisionError:
       print("Erro, divisao com zero nao é valida")
       continue



    print(f"Resultado: {a} {op} {b} = {resultado}")
    print("-" * 30)

    if not sair():
        break