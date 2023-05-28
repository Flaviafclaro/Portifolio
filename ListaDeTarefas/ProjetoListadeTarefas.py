# Projeto Lista de Tarefas

from datetime import datetime

def validar_data(data_hora):
    try:
        datetime.strptime(data_hora, "%d/%m/%Y %H:%M")  # Verifica se a data e hora seguem o formato especificado
        return True
    except ValueError:
        return False

def adicionar_tarefa(nome, descricao, data, hora, lista):
    lista.append(nome + "; " + descricao + "; " + data + "; " + hora)  # Adiciona uma nova tarefa à lista
    
def listar_tarefas(lista):
    for i, tarefa in enumerate(lista):
        print(f"Tarefa número: {i+1}")  # Imprime o número da tarefa
        print("-"*30)
        informacoes = tarefa.split(";")  # Divide as informações da tarefa em uma lista
        print(f"Nome: {informacoes[0]}")  # Imprime o nome da tarefa
        print(f"Descrição: {informacoes[1]}")  # Imprime a descrição da tarefa
        print(f"Data: {informacoes[2]}")  # Imprime a data da tarefa
        print(f"Hora: {informacoes[3]}")  # Imprime a hora da tarefa
        print("\n")
        
def listar_tarefas4(lista): #função para a opção 4 onde não aparece o número da tarefa
    for i, tarefa in enumerate(lista):
        print("-"*30)
        informacoes = tarefa.split(";")
        print(f"Nome: {informacoes[0]}")
        print(f"Descrição: {informacoes[1]}")
        print(f"Data: {informacoes[2]}")
        print(f"Hora: {informacoes[3]}")
        print("\n")
    
lista = []

#Menu do Programa
while True:
     print("\nMenu:")
     print("1. Adicionar uma tarefa")
     print("2. Listar tarefas")
     print("3. Remover uma tarefa")
     print("4. Editar uma tarefa")
     print("5. Sair")
     print("\n")
    
     # Tratando a escolha do usuário detectando se foi digitado um valor inválido
     try:
         escolha = int(input("Escolha: "))  # Lê a escolha do usuário
     except:
         print("Opção inválida, escolha um número da lista!")
         continue
    
     # Escolhendo a opção 1 "Adicionar Tarefa"
     if escolha == 1:
         nome_tarefa = input("Digite o nome da tarefa: ")  # Lê o nome da tarefa
         descricao_tarefa = input("Digite a descrição da tarefa: ")  # Lê a descrição da tarefa
         data_tarefa = input("Digite a data da tarefa (formato DD/MM/YYYY): ")  # Lê a data da tarefa
         hora_tarefa = input("Digite o horário da tarefa (formato: HH:MM): ")  # Lê a hora da tarefa
        
         data_hora = data_tarefa + " " + hora_tarefa
         
         if validar_data(data_hora): 
            adicionar_tarefa(nome_tarefa, descricao_tarefa, data_tarefa, hora_tarefa, lista)
            # print (lista)
         else:
            print("Erro, data ou hora inválida")
     # Escolhendo a opção 2 "Listar Tarefas"
     elif escolha == 2: 
         listar_tarefas(lista)
     
     # Escolhendo a opção 3 "Remover Tarefa"    
     elif escolha == 3:
         listar_tarefas(lista)
         try:
             num_tarefa = int(input("Digite o número da tarefa: "))  # Lê o número da tarefa a ser removida
             if num_tarefa <=0 or num_tarefa > len(lista):
                 print("Número de tarefa inválido!")
                 continue
             del lista[num_tarefa - 1]
             print (f"Tarefa {num_tarefa} removida!")
            
         except ValueError:
             print("Escolha um  número válido de tarefa (consulte listar tarefas - opção 2)")
             
     # Escolhendo a opção 4 "Editar Tarefa"
     elif escolha == 4:
        listar_tarefas(lista)
        try:
            num_tarefa = int(input("Digite o número da tarefa a ser editada: "))  # Lê o número da tarefa a ser editada
            if num_tarefa <= 0 or num_tarefa > len(lista):
                print("Número de tarefa inválido!")
                continue

            # Edição da tarefa onde é possível alterar todos os campos da tarefa escolhida
            nova_descricao = input("Digite a nova descrição da tarefa: ")
            lista[num_tarefa - 1] = lista[num_tarefa - 1].split(";")
            lista[num_tarefa - 1][1] = nova_descricao
            lista[num_tarefa - 1] = ";".join(lista[num_tarefa - 1])
            
            nova_data = input("Digite a nova data da tarefa: ")
            lista[num_tarefa - 1] = lista[num_tarefa - 1].split(";")
            lista[num_tarefa - 1][2] = nova_data
            lista[num_tarefa - 1] = ";".join(lista[num_tarefa - 1])
            
            nova_hora = input("Digite a novo horário da tarefa: ")
            lista[num_tarefa - 1] = lista[num_tarefa - 1].split(";")
            lista[num_tarefa - 1][3] = nova_hora
            lista[num_tarefa - 1] = ";".join(lista[num_tarefa - 1])
            
            print("\n")
            print(f"Tarefa {num_tarefa} foi atualizada!")
            listar_tarefas4([lista[num_tarefa - 1]])
            
        except ValueError:
            print("Escolha um número inteiro")
    # Escolhendo a opção 5 "Sair do Programa"         
     elif escolha == 5:
         print("Saindo do programa...")
         break
