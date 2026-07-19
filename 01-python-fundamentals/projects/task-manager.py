# Adicionando tarefas
def adicionar_tarefa(tarefas, nome_tarefa):

  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  return


# Visualizando tarefas
def ver_tarefas(tarefas):
  print("\nLista de tarefas:")

  for index, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else ""
    nome_tarefa = tarefa['tarefa']
    print(f"{index}. [{status}] {nome_tarefa}")
  
  return


# Atualizando uma tarefa
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):

  indice_tarefa_ajustado = int(indice_tarefa) - 1

  # evitando que o índice seja inválido
  if (indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas)):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")

  else:
    print("Índice de tarefa inválido")
  
  return


# Completando uma tarefa
def completar_tarefa(tarefas, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_ajustado]["completada"] = True
  print(f"Tarefa {indice_tarefa} marcada como completada")


# Excluindo uma tarefa completada

def deletar_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if tarefa["completada"]:
      tarefas.remove(tarefa)
  
  print("Tarefas completadas foram deletadas.")

  return 


# Lista de tarefas
tarefas = []

while True:
  print("\nMenu do Gerenciador de Lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar Tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas completas")
  print("6. Adicionar tarefa")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:")
    adicionar_tarefa(tarefas, nome_tarefa)
  
  elif escolha == "2":
    ver_tarefas(tarefas)

  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
    completar_tarefa(tarefas, indice_tarefa)

  elif escolha == "5":
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)

  elif escolha == "6":
    break


print ("Programa finalizado.")



