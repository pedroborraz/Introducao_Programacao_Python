# faz a divisao inteira do primeiro numero pelo segundo e mostra o resto, usando while e operadores aritmeticos(-, +)


num1 = int(input("Digite o primeiro numero(dividendo): "))
num2 = int(input("Digite o segundo numero(divisor): "))

if (num2 == 0):
    print("Divisao por zero nao e permitida.")
else:
    quociente = 0 
    resto = num1

    while (resto >= num2):
        resto -= num2
        quociente += 1

    print(f"Divisao inteira: {quociente}")
    print(f"Resto: {resto}")

    # na mat. o quociente e o numero de vezes que o divisor cabe no dividendo o resto e o que sobra apos isso