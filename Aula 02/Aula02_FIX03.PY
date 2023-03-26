numero_recebido = 0
resultado_modulo = 0 

numero_recebido = int(input("\nDigite o número que deseja descobrir se é par ou ímpar: \n\n"))

resultado_modulo = numero_recebido % 2

if resultado_modulo == 0:
    print("O número apresentado é par")
else: 
    print("O número apresentado é ímpar")