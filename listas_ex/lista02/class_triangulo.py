lado1 = float(input("Digite o valor do primeiro lado do triangulo: "))
lado2 = float(input("Digite o valor do segundo lado do triangulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triangulo: "))

if (lado1 == lado2 and lado2 == lado3):
    print("Esse triangulo e equilatero")
elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("Esse triangulo e isosceles")
else:
    print("Esse triangulo e escaleno")