produto = "produto"
valor = 0
qtd = 0
valor_final = 0
tipo_pgto = "n" #tipos de pagamento podem ser s para sim e n para não
percent_desconto = 0.15
valor_desconto = 0

#exercicio de fixação 05 da aula 01

print("Calculadora soma de PRODUTOS \n")

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor individual deste produto: "))
qtd = int(input("Digite a quantidade desejada: "))

valor_final = valor * qtd;

print("O valor total dos produtos é: ", valor_final)

tipo_pgto = input("O pagamento será à vista? s/n: ")
                
if tipo_pgto == 's' :
    valor_desconto = valor_final * percent_desconto;
    valor_final = valor_final - valor_desconto;
    print("O valor final recebeu um desconto de 15% totalizando: ", valor_final)
else tipo_pgto == 'n':
    print("O valor final irá se manter sem desconto: ", valor_final)