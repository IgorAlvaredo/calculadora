Como usar a calculadora

1.   Abra o terminal do linux
2.   Encontre o diretório do arquivo calculadora.sh
3.   Caso precise alterar o caminho da calculadora.py, digite "nano (caminho da calculadora.sh)" e na ultima linha que faz a execução da calculadora.py, altere o diretório após o comando python3 e salve a edição
4.   Agora precisamos permitir que o arquivo .sh seja execultado, para isso basta colocar o comando chmod +x calculadora.sh
5.   após isso execulte o script da calculadora com o comando "./calculadora.sh"

Como o codigo da calculadora.py funciona

*   O primeiro comando é um "while True", que tem o objetivo de fazer um loop infinito, querando apenas quando o usuario digitar que quer sair no fim do loop.
*   logo em seguida pegamos "num1" e "num2" que recebem o numero que o usuario digita e já converte em float.
*   Após isso, é mostrada todas as operações disponiveis que são "+", "-", "x", "/", e pede para o usuario escrever o simbolo relacionado a operação solicitada, a variavel "op" recebe a operação.
*   Inicializo a variavel "resultado" como um float.
*   Após receber a operação seguimos para um if else em sequencia, fazendo o teste, para saber se a operação existe e caso exista muda o valor da variavel resultado com o resultado da operação.
*   Ao realizar a operação, coloco um "print()" e mostro qual foi a operação e o resultado.
*   Após mostrar o resultado, foi colocado uma pergunta para se o usuario deseja fazer uma nova operação ou sair, escolhendo sair é utilizado o comando "break" para encerrar a calculadora, ma se a resposta for não o laço se repete assim recomeçando o fluxo.
