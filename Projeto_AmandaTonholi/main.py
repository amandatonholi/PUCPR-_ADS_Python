#Projeto de Software - ADSPUCPR

#Biblioteca Imports
import time

#Semana 02 - Criação do Menu

#___________________________________________________________________________________________________________________________________
# Menu Principal

print("\nBem-vindo ao Menu PRINCIPAL! Digite uma opção válida e aperte ENTER no final:\n")
print("1. Gestão de Estudantes")
print("2. Gestão de Disciplinas")
print("3. Gestão de Professores")
print("4. Gestão de Turmas")
print("5. Gestão de Matrículas")
print("0. Sair do Sistema")
opcao_menu_principal = int(input("\nOpção desejada: "))

if opcao_menu_principal == 1:
    texto_menu_principal = "Gestão de ESTUDANTES"
elif opcao_menu_principal == 2: 
    texto_menu_principal = "Gestão de DISCIPLINAS"
elif opcao_menu_principal == 3:
    texto_menu_principal = "Gestão de PROFESSORES"
elif opcao_menu_principal == 4:
    texto_menu_principal = "Gestão de TURMAS"
elif opcao_menu_principal == 5:
    texto_menu_principal ="Gestão de MATRÍCULAS"
elif opcao_menu_principal == 0:
    print("\nSaindo...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    texto_menu_principal = "Sair"
else:
    texto_menu_principal = "Valor Inválido, Tente Novamente"

#___________________________________________________________________________________________________________________________________
# Menu Operacional

if texto_menu_principal != "Sair" :
    print("\nBem-vindo ao Menu OPERAÇÕES da", texto_menu_principal, "! Digite uma opção válida e aperte ENTER no final:\n")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Exluir ")
    print("5. Matrículas")
    print("0. Voltar Menu Anterior")
    opcao_menu_operacional = int(input("\nOpção desejada: "))



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
else:
    time.sleep(1)
    print("\nAplicação Encerrada!\n")