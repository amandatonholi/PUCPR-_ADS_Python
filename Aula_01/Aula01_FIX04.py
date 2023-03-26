produto = "produto"
valor = 0
qtd = 0
valor_final = 0

#exercicio de fixação 04 da aula 01

print("Calculadora soma de PRODUTOS \n")

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor individual deste produto: "))
qtd = int(input("Digite a quantidade desejada: "))

valor_final = valor * qtd;
print("O valor total dos produtos é: ", valor_final)