"""Calculadora salario bruto e descontos"""

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite o numero de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"\nSalario Bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"Salario Liquido: R$ {salario_liquido:.2f}\n")