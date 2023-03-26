lado01 = 0
lado02 = 0
lado03 = 0
soma_lados = 0
validacao_triangulo = ""

lado01 = float(input("\nInforme o valor do primeiro lado do triângulo:\n"))
lado02 = float(input("\nInforme o valor do segundo lado do triângulo:\n"))
lado03 = float(input("\nInforme o valor do terceiro lado do triângulo:\n"))

soma_lados_poss1 = lado01 + lado02
soma_lados_poss2 = lado02 + lado03
soma_lados_poss3 = lado03 + lado01

if soma_lados_poss1 > lado03:
    validacao_triangulo = "VERDADEIRA"
elif soma_lados_poss2 > lado01:
    validacao_triangulo = "VERDADEIRA"
elif soma_lados_poss3 > lado02:
    validacao_triangulo = "VERDADEIRA"
else:
    print("Esses valores não indicam ser um triângulo")

print("\n\nDe acordo com esses valores a afirmação de EXISTE UM TRIÂNGULO É: ", validacao_triangulo)

if lado01 == lado02 == lado03: 
    print("\nEste é um triângulo EQUILÁTERO\n")
elif lado01 != lado02 != lado03:
    print("\nEste é um triângulo ESCALENO\n")
else:
    print("\nTipo de triângulo ISÓCELES\n")
