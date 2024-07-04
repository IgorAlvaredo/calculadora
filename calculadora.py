while True:
  num1 = float(input('Digite o primeiro numero para operação: '))
  num2 = float(input('Digite o segundo numero para a operação: '))
  print("")
  print('Qual operação deseja usar? \n'
  "digite '+' para adição \n"
  "digite '-' para subtração \n"
  "digite 'x' para multiplicação \n"
  "digite '/' para divisão \n")

  op = input('')
  resultado = float(0)
  if op == '+':
    resultado = num1 + num2
  elif op == '-':
     resultado = num1 - num2
  elif op == 'x' or op =='X':
     resultado = num1 * num2
  elif op == '/':
     resultado = num1 / num2
  else:
    print("Error! operação inválida")

  print(f'O resultado da operação {num1} {op} {num2} = {resultado}')

  resp = input("Deseja encerrar a calculadora?\n"
  "Digite 'S' para Sim, 'N' para Não\n")

  if(resp == 's' or resp == 'S'):
    break
  elif(resp == 'n' or resp == 'N'):
    print("\n\n\n")
    continue