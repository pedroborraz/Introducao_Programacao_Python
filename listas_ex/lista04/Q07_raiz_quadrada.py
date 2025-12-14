# metodo de newton para calcular raiz quadrada

num = float(input("Digite um numero para calcular a raiz quadrada: "))
base = 2
aprox = ( base + num / base ) / 2

while (abs( base - aprox) >= 0.0001): # tolerancia de 0.0001
    base = aprox
    aprox = ( base + num / base ) / 2

print(f"A primeira aproximacao da raiz quadrada de {num} e {base}, a segunda aproximacao e {aprox}")

# a aproximacao sofre por conta da tolerancia e pela precisao dos numeros de ponto flutuante