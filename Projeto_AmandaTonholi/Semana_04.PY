#Projeto de Software - ADSPUCPR

#Biblioteca Imports
import time

#Semana 02 - Criação do Menu

#___________________________________________________________________________________________________________________________________
#Função de Estudantes

lista_de_alunos = []

def incluir_aluno(nome_do_aluno):
   lista_de_alunos.append(nome_do_aluno)

def listar_alunos ():
    print(lista_de_alunos)

#___________________________________________________________________________________________________________________________________
# Menu Principal

while True:

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
        time.sleep(1)
        print("\n  Etapa Em DESENVOLVIMENTO")
        break
    elif opcao_menu_principal == 3:
        texto_menu_principal = "Gestão de PROFESSORES"
        time.sleep(1)
        print("\n  Etapa Em DESENVOLVIMENTO")
        break
    elif opcao_menu_principal == 4:
        texto_menu_principal = "Gestão de TURMAS"
        time.sleep(1)
        print("\n  Etapa Em DESENVOLVIMENTO")
        break
    elif opcao_menu_principal == 5:
        texto_menu_principal ="Gestão de MATRÍCULAS"
        time.sleep(1)
        print("\n  Etapa Em DESENVOLVIMENTO")
        break
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
        print("4. Excluir ")
        print("5. Matrículas")
        print("0. Voltar Menu Anterior")
        opcao_menu_operacional = int(input("\nOpção desejada: "))

        #inclusão de alunos na lista de registros
        if opcao_menu_operacional==1: 
            nome_do_aluno = input("\nInsira nome do aluno a ser registrado: ")
            incluir_aluno(nome_do_aluno)
            print("Registro Incluído com Sucesso")
            retorno_ao_menu = input("Deseja voltar ao menu anterior? Digite apenas a inicial s-sim e n-não")
            if retorno_ao_menu == "s": 
                
            else:

        #opção de listagem dos alunos 
        elif opcao_menu_operacional==2:
            print("Os alunos registrados atualmente na base são: \n")
            listar_alunos()

        #opção de atualização dos dados do aluno
        elif opcao_menu_operacional==3:
            time.sleep(1)
            print("Em Desenvolvimento")
            break
        
        #opção de excluir registro do aluno da lista 
        elif opcao_menu_operacional==4:
            time.sleep(1)
            print("Em Desenvolvimento")
            break

        elif opcao_menu_operacional==5:
            time.sleep(1)
            print("Em Desenvolvimento")
            break
        else:
            print ("Retornando ao menu anterior")
            time.sleep(1)
            
    else:
        time.sleep(1)
        print("\nAplicação Encerrada!\n")

print("\nEncerrando Aplicação...")
time.sleep(1) 
print("\nAplicação Encerrada!\n")

