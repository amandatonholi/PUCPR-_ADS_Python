nome_cliente = ""
tamanho_nome_cliente = 0
tamanho_maximo_de_nome = 0

nome_cliente = input("\nDigite o nome que deseja registrar no cartão: \n\n")

tamanho_maximo_de_nome = 20
tamanho_nome_cliente = int(len(nome_cliente))

if tamanho_nome_cliente <= tamanho_maximo_de_nome :

    print("Ok, Nome registrado no cartão com sucesso")

else: 
    
    print("Nome com mais de 20 caracteres, tamanho não permitido. Tente Novamente")