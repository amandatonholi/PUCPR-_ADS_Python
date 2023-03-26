salario_inicial = 0
valor_abono =0
salario_final = 0
percent_abono = 0
valor_limite_salario = 5000.00

salario_inicial = float(input("\nDigite o valor do seu salário\n\n"))

if salario_inicial >= valor_limite_salario : 
    percent_abono = 0.10
    valor_abono = salario_inicial * percent_abono
    salario_final = salario_inicial + valor_abono
    print("\nSeu salário no final do ano será de: ", salario_final)
else:
    percent_abono = 0.15
    valor_abono = salario_inicial * percent_abono
    salario_final = salario_inicial + valor_abono
    print ("\nSeu salário no final do ano será de: ", salario_final)


