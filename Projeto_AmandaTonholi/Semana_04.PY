#Projeto de Software - ADSPUCPR

#Biblioteca Imports
import time

#Semana 02 - Criação do Menu

#___________________________________________________________________________________________________________________________________
#Declaração de variáveis 
opcao_menu_principal=0
opcao_menu_operacional=0

#___________________________________________________________________________________________________________________________________
#Função de Estudantes

lista_de_alunos = []

def incluir_aluno(nome_do_aluno):
   lista_de_alunos.append(nome_do_aluno)

def listar_alunos ():
    print(lista_de_alunos)


#___________________________________________________________________________________________________________________________________
# Função Menu Principal

def menu_principal():

    print("\nBem-vindo ao Menu PRINCIPAL! Digite uma opção válida e aperte ENTER no final:\n")
    print("1. Gestão de Estudantes")
    print("2. Gestão de Disciplinas")
    print("3. Gestão de Professores")
    print("4. Gestão de Turmas")
    print("5. Gestão de Matrículas")
    print("0. Sair do Sistema")

#___________________________________________________________________________________________________________________________________
# Função Menu Operacional
def menu_operacional():

    print("\nBem-vindo ao Menu OPERAÇÕES! Digite uma opção válida e aperte ENTER no final:\n")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir ")
    print("5. Matrículas")
    print("0. Voltar Menu Anterior")


#___________________________________________________________________________________________________________________________________
# Navegação nos Menus
execucao = True

while execucao:
    menu_principal ()
    opcao_menu_principal = int(input("\nOpção desejada: "))
    if opcao_menu_principal == 1:
        menu_operacional()
        opcao_menu_operacional = int(input("\nOpção desejada: "))

        if opcao_menu_operacional == 1:
            nome_do_aluno = input("\nInsira nome do aluno a ser registrado: ")
            incluir_aluno(nome_do_aluno)
            print("\nRegistro Incluído com Sucesso")

            retornar = input("\nDeseja realizar outra operação? Digite apenas a inicial s-sim ou n-não:  ")
            if retornar == "n":
                execucao = False 
                                    
        elif opcao_menu_operacional == 2:
            print("\nOs alunos registrados atualmente na base são: \n")
            listar_alunos()

            retornar = input("\nDeseja realizar outra operação? Digite apenas a inicial s-sim ou n-não:  ")
            if retornar == "n":
                execucao = False 

        elif opcao_menu_principal == 2: 
            time.sleep(1)
            print("\n  Etapa Em DESENVOLVIMENTO")

        elif opcao_menu_principal == 3:
            time.sleep(1)
            print("\n  Etapa Em DESENVOLVIMENTO")
            
        elif opcao_menu_principal == 4:
            time.sleep(1)
            print("\n  Etapa Em DESENVOLVIMENTO")
            
        elif opcao_menu_principal == 5:
            time.sleep(1)
            print("\n  Etapa Em DESENVOLVIMENTO")

        elif opcao_menu_principal == 0:
            print("\nSaindo...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            
        else:
            print("Valor Inválido, Tente Novamente")
                
print("\nEncerrando Aplicação...")
time.sleep(1)
print("\nSaindo...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("\nAplicação Encerrada!\n")

