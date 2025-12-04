valor_produto = float(input("Digite o valor do produto: R$"))
forma_pagamento = input("Digite a forma de pagamento (D para dinheiro e C para cheque): ")

if (valor_produto >= 100 and forma_pagamento.upper() == "D"):
    print(f"Voce ganhou 10% de desconto, o produto ficou por {(valor_produto * 0.9):.2f}")
elif (forma_pagamento.upper() == "C"):
    print(f"Voce nao tem desconto, o produto ficou por {valor_produto:.2f}")
else:
    print("Forma de pagamento invalida")