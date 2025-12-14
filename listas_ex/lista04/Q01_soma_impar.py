# soma de todos os numeros impares multiplos de 3 entre 1 e 500


soma = 0
num = 1

while (num <= 500):
    if (num % 2 != 0 and num % 3 == 0):
        soma += num
    num += 1

print("A soma dos numeros impares multiplos de 3 entre 1 e 500 e:",soma)