turno = input("Qual turno que voce estuda? (M)atutino, (V)espertino ou (N)oturno: ")

if (turno.upper() == "M"):
    print("Bom dia!")
elif (turno.upper() == "V"):
    print("Boa tarde!")
elif (turno.upper() == "N"):
    print("Boa Noite")
else:
    print("Valor invalido")