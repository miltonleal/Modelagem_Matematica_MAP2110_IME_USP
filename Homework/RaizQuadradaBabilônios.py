#lê o valor que se deseja calcular a raiz quadrada
n = float(input("Digite o número que deseja calcular a raiz quadrada: "))
x = n

#lê o quadrado perfeito mais próximo do número que se deseja calcular a raiz quadrada
y = int(input("Insira o número mais próximo do resultado: "))

#define a precisão do resultado
e = float(input("Qual a precisão desejada para o resultado? "))

#realiza o cálculo com base no método babilônico
while (x - y > e):
        x = (x + y) / 2
        y = n / x

        print ("A raiz quadrada de", n, "é:", x)

