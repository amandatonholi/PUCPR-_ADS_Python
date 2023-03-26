#Projeto de Software - ADSPUCPR

#Biblioteca Imports
import time

#Semana 02 - Criação do Menu

#___________________________________________________________________________________________________________________________________
# Menu Principal
retornar = True

while retornar == True:

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

        if opcao_menu_operacional==1 or opcao_menu_operacional==2 or opcao_menu_operacional==3 or opcao_menu_operacional==4 or opcao_menu_operacional==5:
            print("\nLegal, logo iremos descobrir como fazer isso, por enquanto é isso! Obrigada.\n")
            time.sleep(1)
            print("\nEncerrando Aplicação...")
            time.sleep(2)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("\nAplicação Encerrada!\n")
            retornar = False

        else:
            print ("Retornando ao menu anterior")
            time.sleep(1)
            
    else:
        time.sleep(1)
        print("\nAplicação Encerrada!\n")