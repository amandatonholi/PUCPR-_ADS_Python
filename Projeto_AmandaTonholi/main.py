#Projeto de Software - ADSPUCPR

#Semana 02 - Criação do Menu

#Menu Principal 

print("\nBem-vindo ao Menu Principal do Sistema! Digite uma opção válida e aperte ENTER no final:\n")
opcao_menu = int(input(" 1. Incluir Registro \n
                         2. Alterar Registro 
                       \n 3. Excluir Registro 
                       \n 4. Listar Registros Disponíveis 
                       \n 0. Sair \n"))

#Incluir registro
if opcao_menu == 1 :
    print("Para o incluir um novo registro de estudante vamos precisar de:\n")
    nome_estudante = input("Digite o nome do estudante: ")
    cod_matricula = int(input("Digite o código de matrícula somente números com até 5 casas: "))

#Alterar Registro 
elif opcao_menu == 2 :
    print("entrar menu 2")

##Excluir Registro
elif opcao_menu == 3 :
    print("entrar menu 3")

#Listar Registros Disponíveis
elif opcao_menu == 4 :
    print("entrar menu 4")

##Sair do Menu
elif opcao_menu == 0 :
    print("Saindo....\n")
    print("Obrigada pela sua participação")

else:
    print ("Opção Inválida, tente novamente")