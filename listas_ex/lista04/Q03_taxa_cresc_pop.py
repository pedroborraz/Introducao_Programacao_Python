# numero de anos para a populacao do pais X ultrapassar a do pais Y, seguindo uma taxa de crescimento anual constante


populacao_X = 70000
populacao_Y = 180000
taxa_crescimento_X = 0.035
taxa_crescimento_Y = 0.015 
anos = 0

while (populacao_X <= populacao_Y):
    populacao_X += populacao_X * taxa_crescimento_X
    populacao_Y += populacao_Y * taxa_crescimento_Y
    anos += 1

print(f"Serao necessarios {anos} anos para a populacao do pais X ultrapassar a do pais Y.")