import datetime

def validar_horas(data_horass):
  try:
    datetime.strptime(data_horas, "%d/%m/%y %H:%M ")
    return True
  except:
    return False


print("olá bem vindo a lista do senpai")
print("")
menu = """[1] para adicionar compromissos
[2] Remover compromissos da lista 
[3] Listar compromissos
[4] Iditar compromissos"""
lista = []
while True:
  print(menu)
  print("")
  try:
    opcao = int(input("qual sua escola? :"))
  except ValueError:
    print("opção invalida")
    print("")
    continue
  if opcao == 1:
    nome_tarefas = input("qual o nome da tarefa ")
    descricao_tarefas = input("qual a descrição da tarefa")
    datas_tarefas = input("qual a data ex: dias mês e ano")
    hora_tarefa = input("qual a hora da tarefa")
    
    data_horas = datas_tarefas + "" + hora_tarefa
    
    if (validar_horas(data_horas)):
      print("su")
    else:
      print("error")
  