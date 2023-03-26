turno = input("Qual turno você trabalha? \n (Retorne apenas a inicial: m-manhã | t-tarde | n-noite)\n\n")

if turno == "m" : 
    print("\nTenha um Bom dia e um ótimo trabalho\n\n")
elif turno == "t":
    print("\nTenha uma boa tarde e um ótimo trabalho\n\n")
elif turno == "n": 
    print("\nTenha uma boa noite e um ótimo trabalho\n\n")
else:
    print("\nEntrada inválida, tente novamente\n\n")