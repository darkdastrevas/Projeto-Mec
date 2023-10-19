#Função exibir_menu:
def exibir_menu():
  print('=' * 50)
  print('Bem vindo ao sistema de bilheteria do cinema!')
  print('=' * 50)
  print("""[1] - Cadastrar sala
[2] - Atualizar sala
[3] - Remover sala 
[4] - Emitir ingresso
[5] - Visualizar todas as salas
[6] - Filtras filmes
""")

# Função Adicionar Sala
def adicionar_sala(cinema, numero_sala, filme, genero, idade_minima, data_saida):
  sala = [numero_sala, filme, genero, idade_minima, 50, data_saida]
  cinema.append(sala)
  print(f'Sala {numero_sala} adicionada com sucesso!')

# Função Atualizar Sala
def atualizar_filme(cinema, numero_sala):
  for i in cinema:
    if i[0] == numero_sala:
      i[1] = input("Digite o nome do filme: ")
      i[2] = input("Digite o gênero do filme: ")
      i[3] = input("digite a idade mínima para assistir ao filme: ")
      i[5] = input("digite a data de saída do filme: ")
  print(f'Sala {numero_sala} atualizada com sucesso!'	)

#Data
def formatar_data(data_saida):
  while len(data_saida) != 8 or not data_saida.isdigit():
      print('Formato de data incorreto!')
      data_saida = input('Data de saída (ddmmaaaa): ')
  return data_saida[:2] + '-' + data_saida[2:4] + '-' + data_saida[4:]
  
#Remover Sala
def remover_sala(cinema, numero_sala):
  for i in cinema:
    if i[0] == numero_sala:
      cinema.remove(i)
      print(f'Sala {numero_sala} removida com sucesso!')
    elif numero_sala not in i:
      print(f'Sala {numero_sala} não encontrada!')
      return