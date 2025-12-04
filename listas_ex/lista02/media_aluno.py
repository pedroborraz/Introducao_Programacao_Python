nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 9):
    print(f"Sua media e {media:.2f} com o conceito A")
elif (media >= 7.5):
    print(f"Sua media e {media:.2f} com o conceito B")
elif (media >= 6):
    print(f"Sua media e {media:.2f} com o conceito C")
elif (media >= 4):
    print(f"Sua media e {media:.2f} com o conceito D")
else:
    print(f"Sua media e {media:.2f} com o conceito E")