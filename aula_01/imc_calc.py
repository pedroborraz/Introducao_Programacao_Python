"""Calculadora de IMC para homens e mulheres"""

altura = float(input("Digite a sua altura em metros: "))
homem = 72.7 * altura - 58
mulher = 62.1 * altura - 44.7
print(f"O peso ideal para homens é: {homem:.2f} kg")
print(f"O peso ideal para mulheres é: {mulher:.2f} kg")