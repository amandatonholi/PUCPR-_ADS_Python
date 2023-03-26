numero_01 = 0
numero_02 = 0
operacao = ""
resultado = 0

numero_01 = float(input("\nDigite o primeiro valor: \n"))
numero_02 = float(input("\nDigite o segundo valor: \n"))
operacao = input("\nDigite a operação que deseja realizar:\n")

if operacao == "+":
    resultado = numero_01 + numero_02
    print("\n\nSeu cálculo foi: \n", resultado, "=", numero_01, "+", numero_02,"\n\n")
elif operacao == "-":
    resultado = numero_01 - numero_02
    print("\n\nSeu cálculo foi: \n", resultado, "=", numero_01, "-", numero_02,"\n\n")
elif operacao == "/":
    resultado = numero_01 / numero_02
    print("\n\nSeu cálculo foi: \n", resultado, "=", numero_01, "/", numero_02,"\n\n")
elif operacao == "*":
    resultado = numero_01 * numero_02
    print("\n\nSeu cálculo foi: \n", resultado, "=", numero_01, "*", numero_02,"\n\n")
else:
    print ("\nTente Novamente\n\n")